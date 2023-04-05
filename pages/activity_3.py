import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
from io import BytesIO

def read_image(file):
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def reflect_image(img):
    rows, cols, ch = img.shape
    m_reflection=np.float32([[1, 0, 0], [0,-1,rows],[0,0,1]])
    reflected_img=cv2.warpPerspective(img,m_reflection,(int(cols),int(rows)))
    plt.axis('off')
    plt.imshow(reflected_img)
    return plt.gcf()

def rotate_image(img, angle):
    rows, cols, ch = img.shape
    angle = np.radians(angle)
    m_rotation = np.float32([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])
    rotated_img = cv2.warpPerspective(img, m_rotation, (cols, rows))
    plt.axis('off')
    plt.imshow(rotated_img)
    return plt.gcf()

def shear_image(img, shear_factor):
    rows, cols, ch = img.shape
    m_shearing = np.float32([[1, shear_factor, 0], [0, 1, 0], [0, 0, 1]])
    sheared_img = cv2.warpPerspective(img, m_shearing, (int(cols * (1 + abs(shear_factor))), rows))
    plt.axis('off')
    plt.imshow(sheared_img)
    return plt.gcf()

def translate_image(img, x_offset, y_offset):
    rows, cols, channels = img.shape
    M = np.float32([[1, 0, x_offset], [0, 1, y_offset]])
    translated_img = cv2.warpAffine(img, M, (cols, rows))
    plt.imshow(translated_img)
    plt.axis('off')
    return plt.gcf()

# Streamlit code
st.title("Image Manipulation")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load an image
    img = read_image(uploaded_file)

    # Reflect the image
    st.subheader("Reflected Image")
    fig_reflect = reflect_image(img)
    st.pyplot(fig_reflect)

    # Rotate the image
    st.subheader("Rotated Image")
    fig_rotate = rotate_image(img, 10)
    st.pyplot(fig_rotate)

    # Shear the image
    st.subheader("Sheared Image")
    fig_shear = shear_image(img, 0.5)
    st.pyplot(fig_shear)

    # Translate the image
    st.subheader("Translated Image")
    x_offset = st.slider("X Offset", -img.shape[1], img.shape[1], 0)
    y_offset = st.slider("Y Offset", -img.shape[0], img.shape[0], 0)
    fig_translate = translate_image(img, x_offset, y_offset)
    st.pyplot(fig_translate)