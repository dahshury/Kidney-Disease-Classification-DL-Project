import streamlit as st
import time
from CNNClassifier.pipeline.prediction import PredictionPipeline

st.write("<h1 style='text-align: center';>Kidney Disease Classifier</h1>", unsafe_allow_html=True)
colA,colB,colC = st.columns(3)
colB.image("./dataset-card.png", use_column_width=True)  # Display image in the column
st.write("Possible classes:")
all_classes = ["Cyst", "Normal", "Stone", "Tumor"]

# Displaying the possible classes as a JSON block
classes_dict = {f"Class {idx}": class_name for idx, class_name in enumerate(all_classes)}
st.json(classes_dict)
img = st.file_uploader("Please upload a CT scan of a kidney", type=("JPG", "PNG", "JPEG", "webp"))

if img:
    col1, col2 = st.columns(2)

    # Display image in col1
    col1.image(img, width=300)

    # Create empty placeholder for spinner in col2
    with col2:
        spinner = st.empty()

        with st.spinner("Predicting..."):
            result = PredictionPipeline(img=img).predict_streamlit()

    # Clear the spinner and display results in col2
    spinner.empty()
    col2.json(result)
