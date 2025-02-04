# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sdf-EUmFD6-0Rx0usMyDZkeifFS5UcyX
"""

import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Load CNN model
model = load_model("model_cnn.h5")

# Predict Model
# def process_and_predict(file):
#     im = Image.open(file).convert("RGB")
#     width, height = im.size
#     if width == height:
#         im = im.resize((200,200), Image.LANCZOS)
#     else:
#         if width > height:
#             left = int((width - height) / 2)
#             right = int((width + height) / 2)
#             top = 0
#             bottom = height
#             im = im.crop((left,top,right,bottom))
#             im = im.resize((200,200), Image.LANCZOS)
#         else:
#             left = 0
#             right = width
#             top = 0
#             bottom = width
#             im = im.crop((left,top,right,bottom))
#             im = im.resize((200,200), Image.LANCZOS)

#     ar = np.asarray(im)
#     ar = ar.astype('float32')
#     ar /= 255.0
#     ar = ar.reshape(-1, 200, 200, 3)

#     pred = model.predict(ar)

#     # Get the index of the highest probability
#     pred_class = np.argmax(pred, axis=-1)  # This returns the index of the highest probability

#     class_index = pred_class[0]
    
#     class_labels = ['Healthy (No Tumor)', 'Pituitary', 'Meningioma', 'Glioma']
#     prediction = class_labels[class_index]

#     # print(f"Type of tumor: {prediction}")
#     return prediction ,im.resize((300,300), Image.LANCZOS)


def process_and_predict(file):
    im = Image.open(file).convert("RGB")
    width, height = im.size

    # Resize while maintaining aspect ratio
    if width != height:
        if width > height:
            left = int((width - height) / 2)
            right = int((width + height) / 2)
            im = im.crop((left, 0, right, height))
        else:
            top = int((height - width) / 2)
            bottom = int((height + width) / 2)
            im = im.crop((0, top, width, bottom))

    im = im.resize((200, 200), Image.LANCZOS)
    
    # Normalize and reshape for CNN
    ar = np.asarray(im).astype('float32') / 255.0
    ar = ar.reshape(-1, 200, 200, 3)

    # Predict
    pred = model.predict(ar)

    # Get predicted class
    pred_class = np.argmax(pred, axis=-1)  # Returns array, needs conversion
    class_index = int(pred_class[0])  # Convert to integer
    
    # Map predicted class to labels
    class_labels = ['Healthy (No Tumor)', 'Pituitary', 'Meningioma', 'Glioma']
    prediction = class_labels[class_index]

    return prediction, im.resize((300, 300), Image.LANCZOS)



# Title
st.title('Brain Tumor Classification App')

st.write('Load an Image:')

# Upload File
uploaded_file = st.file_uploader('Choose an image...', type=["jpg", "jpeg", "png", "gif"])

if st.button('Predict'):
  if uploaded_file is not None:
    pred, img = process_and_predict(uploaded_file)
    st.write(f"Type of tumor: {pred}")
    st.image(img)

  else:
    print('Error: Upload Image file, type=["jpg", "jpeg", "png", "gif"]')

