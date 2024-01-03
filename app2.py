import streamlit as st
import time
from CNNClassifier.pipeline.prediction import PredictionPipeline

st.write("<h1 style='text-align: center';>Kidney disease classifier</h1>", unsafe_allow_html=True)
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
