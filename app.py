import streamlit as st
import cv2
import numpy as np
from PIL import Image

def adjust_contrast(image, alpha):
    new_image = cv2.convertScaleAbs(image, alpha=alpha, beta=0)
    return new_image

st.title("Contrast Manipulation")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Adjust the contrast of the image using the slider below.")
    
    alpha = st.slider("Contrast", 1.0, 3.0, 1.0)
    
    adjusted_image = adjust_contrast(img_array, alpha)
    st.image(adjusted_image, caption='Contrast-Adjusted Image.', use_column_width=True)
