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
    selected_model = models_list[0]
    loaded_model = joblib.load(directory + '/' + selected_model)
    return loaded_model


def upload_number_image():
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        img = img.convert('L')
        img = img.resize((28, 28))
        img = np.bitwise_not(img)
        img = np.array(img, dtype=np.float64)
        image_array = img.flatten()
        model = load_model(os.getcwd() + '/models')
        st.write(model.predict([image_array]))


def draw_number():
    stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 2)
    realtime_update = st.sidebar.checkbox("Update in realtime", True)
    canvas_result = st_canvas(stroke_width=25, stroke_color="#fff", background_color="#000", height=280, width=280, drawing_mode="freedraw", key="canvas",)
    prediction = models.predict(canvas_result.image_data)
    st.write(prediction)


