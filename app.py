from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from CNNClassifier.utils.common import decodeImage
from CNNClassifier.pipeline.prediction import PredictionPipeline
import os
from pathlib import Path

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = FastAPI()
templates = Jinja2Templates(directory="templates")  

# CORS middleware to handle cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you might want to limit this to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

clApp = ClientApp()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/train")
async def train_route():
    # os.system("python main.py")
    os.system("dvc repro")
    return {"message": "Training done successfully!"}

@app.post("/predict")
async def predict_route(request: Request):
    data = await request.json()
    image = data.get('image', None)

    if image is None:
        raise HTTPException(status_code=400, detail="Image not provided")

    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()

    return JSONResponse(content=result)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="app:app", host="0.0.0.0", port=8080, reload=True)
    