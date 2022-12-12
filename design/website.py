from streamlit_drawable_canvas import st_canvas
import streamlit as st
import models.ml_models as models
import os
import joblib
import cv2
from PIL import Image
import numpy as np


def load_model(directory):
    models_list = []
    for file in os.listdir(directory):
        if file.endswith('.sav'):
            models_list.append(file)
    selected_model = st.sidebar.selectbox('Select a model', (models_list))
    loaded_model = joblib.load(directory + '/' + selected_model)
    return loaded_model


def upload_number_image():
    uploaded_image = st.file_uploader("Choose a file")
    if uploaded_image is not None:
        st.image(uploaded_image)
        #img = cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2GRAY)
        st.write(type(uploaded_image))
        image = Image.open(uploaded_image)
        st.image(image)
        image = np.array(image)
        imageprep_2 = cv2.resize(image, (28, 28), interpolation=cv2.INTER_LINEAR)
        imageprep_2 = cv2.bitwise_not(imageprep_2)
        model = load_model(os.getcwd() + '/models')
        imageprep_2 = cv2.cvtColor(imageprep_2, cv2.COLOR_BGR2GRAY)
        imageprep_2 = np.reshape(imageprep_2, (28, 28))
        st.image(imageprep_2)
        st.write(imageprep_2.shape)
        st.write(model.predict(imageprep_2))


def draw_number():
    stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 2)
    realtime_update = st.sidebar.checkbox("Update in realtime", True)
    canvas_result = st_canvas(stroke_width=25, stroke_color="#fff", background_color="#000", height=280, width=280, drawing_mode="freedraw", key="canvas",)
    prediction = models.predict(canvas_result.image_data)
    st.write(prediction)


