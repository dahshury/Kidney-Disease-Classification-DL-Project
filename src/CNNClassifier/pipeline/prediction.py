import numpy as np
from pathlib import Path
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline():
    def __init__(self, filename: str="", img=None):
        self.filename = Path(filename)
        self.img = img
        self.model = load_model(os.path.join("model","model.h5"))
        
    def predict(self):
        imagename = self.filename
        test_image = image.load_img(imagename,  target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(self.model.predict(test_image), axis = 1)
        print(result)
        
        if result[0] == 0:
            prediction = "Cyst"
            return [{"Prediction": prediction}]
        
        elif result[0] == 1:
            prediction = "Normal"
            return [{"Prediction": prediction}]
        
        elif result[0] == 2:
            prediction = "Stone"
            return [{"Prediction": prediction}]
        
        else:
            prediction = "Tumor"
            return [{"Prediction": prediction}]
        
    def predict_streamlit(self):
        test_image = image.load_img(self.img,  target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(self.model.predict(test_image), axis = 1)
        print(result)
        
        if result[0] == 0:
            prediction = "Cyst"
            return [{"Prediction": prediction}]
        
        elif result[0] == 1:
            prediction = "Normal"
            return [{"Prediction": prediction}]
        
        elif result[0] == 2:
            prediction = "Stone"
            return [{"Prediction": prediction}]
        
        else:
            prediction = "Tumor"
            return [{"Prediction": prediction}]