# Importing the required libraries
import cv2
from PIL import Image
from pk_currency_detector import currency
import streamlit as st
import numpy as np 


def detect(cam):
    while True:
        # Reading the image from the webcam
        _, image = cam.read()

        # Converting the image to grayscale
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Detecting the currency
        label = currency(img)

        # Drawing the rectangle In the middle
        cv2.rectangle(image, (150, 150), (450, 350), (0, 255, 0), 2)

        # Displaying the result on the screen
        cv2.putText(image, label, (10, 325), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow('Currency Detection', image)

        # Checking if the user has pressed the escape key
        if cv2.waitKey(1) & 0xFF == 27:
            cam.release()
            cv2.destroyAllWindows()
            exit(0)
        

if __name__ == "__main__":
    # Creating the webcam object
    cam = cv2.VideoCapture(0)

    # Checking if the webcam is opened correctly
    if not cam.isOpened():
        raise IOError("Cannot open webcam")
    detect(cam)