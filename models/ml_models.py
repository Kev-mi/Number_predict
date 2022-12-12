import cv2
import numpy as np
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
import pandas as pd
import os
from skimage.transform import resize
from skimage.io import imread
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from PIL import Image
from numpy import asarray
from sklearn.svm import SVC
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import joblib
import streamlit as st
import design.website as webdesign

def image_prep(img):
    st.image(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    st.image(img)
    imageprep_2 = cv2.resize(img, (28, 28), interpolation=cv2.INTER_LINEAR)
    imageprep_2 = cv2.bitwise_not(imageprep_2)
    st.image(imageprep_2)
    img = np.reshape(imageprep_2, (1, 28 * 28))
    return img


def data_split():
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    return X_train, y_train, X_test, y_test


def data_reshape(X_test, X_train):
    X_train = X_train.reshape(60000, 28 * 28)
    X_test = X_test.reshape(10000, 28 * 28)
    return X_test, X_train


def save_model(grid):
    filename = 'best_model_gridsearch_svm.sav'
    joblib.dump(grid.best_estimator_, filename)


def train_model():
    X_train, y_train, X_test, y_test = data_split()

    param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [0.0001, 0.001, 0.1, 1], 'kernel': ['rbf', 'poly']}
    svc = svm.SVC(probability=False)
    model = GridSearchCV(svc, param_grid)

    X_test, X_train = data_reshape(X_test, X_train)

    steps = [("scaler", StandardScaler()), ("SVM", SVC(kernel="poly"))]
    pipeline = Pipeline(steps)
    parameters = {"SVM__C": [0.001, 0.1, 100, 10 ** 5], "SVM__gamma": [10, 1, 0.1, 0.01]}
    grid = GridSearchCV(pipeline, param_grid=parameters, cv=5)

    grid.fit(X_train, y_train)
    print(grid.score(X_test, y_test))
    print(grid.best_params_)

    y_pred = grid.predict(X_test)

    img = cv2.imread('test_1.png', 0)

    save_model(grid)


def predict(image):
    image = image_prep(image)
    model = webdesign.load_model(os.getcwd() + '/models')
    prediction = model.predict(image)
    st.image(image)
    return prediction[0]
