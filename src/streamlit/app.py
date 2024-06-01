import streamlit as st
# from models.predict_model import predict_image
from PIL import Image
import os

st.title('Plant Disease Detection')

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    # Save the uploaded image
    file_path = os.path.join('/path/to/the/uploads', uploaded_file.name)
    image.save(file_path)
    # Prediction
    # prediction = predict_image(file_path)
    # st.write(f'Prediction: {prediction}')
