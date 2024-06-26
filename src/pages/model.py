from typing import BinaryIO, Optional, Tuple

import streamlit as st
from PIL import Image


def upload_image() -> Tuple[BinaryIO, bool]:
    """
    Uploads an image for classification.

    Returns:
        A tuple containing the uploaded image file and a boolean indicating whether an image was uploaded or not.
    """
    image_present = True

    img_file = st.file_uploader(
        "*Upload an image for classification*",
        type=["jpg", "png"],
    )

    if img_file is None:
        image_present = False
        img_file = open("web/img/no_image_plant.jpg", "rb")

    return img_file, image_present


def prediction():
    """
    Function to perform image prediction and display results.

    Returns:
        None
    """

    st.header("Prediction 🍃")

    st.write("")
    st.subheader("Upload an image")
    st.markdown("*Note: please don't expect too much and don't load strange image.*")

    c1, _, _ = st.columns(3)
    with c1:
        image, image_valid = upload_image()

    img_info = Image.open(image)
    file_details = f"""
        Name: {image.name}
        Type: {img_info.format}
        Size: {img_info.size}
    """

    st.write("")
    st.subheader("Results")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original image ...")

        st.image(img_info, width=150)
        if image_valid:
            st.caption(file_details)

    with col2:
        with st.container():
            st.subheader("... is probably :")

            # Add here the prediction model result.

