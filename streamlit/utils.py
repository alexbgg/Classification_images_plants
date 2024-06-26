import base64
import os
import re
from pathlib import Path
from typing import BinaryIO, Tuple

import numpy as np
import tensorflow as tf

import streamlit as st


########################################################################### Presentation part ###########################################################################


def markdown_images(markdown):
    """
    Main method for converting images for Markdown.

    Args:
        markdown: The document

    Returns:
        images: list of images in the Markdown

    Example:
        >>> ![Test image](images/test.png "Alternate text")
    """
    images = re.findall(
        r'(!\[(?P<image_title>[^\]]+)\]\((?P<image_path>[^\)"\s]+)\s*([^\)]*)\))',
        markdown,
    )
    return images


def img_to_bytes(img_path):
    """
    Converts an image file to a base64-encoded string.

    Args:
        img_path (str): The path to the image file.

    Returns:
        str: The base64-encoded string representation of the image.

    Raises:
        FileNotFoundError: If the image file does not exist.
    """
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


def img_to_html(img_path, img_alt):
    """
    Converts an image file to HTML code for embedding in a webpage.

    Args:
        img_path (str): The path to the image file.
        img_alt (str): The alternative text for the image.

    Returns:
        str: The HTML code for embedding the image.

    Example:
        >>> img_to_html("path/to/image.jpg", "A beautiful sunset")
        '<img src="data:image/jpg;base64,<binary_code>" alt="A beautiful sunset" style="max-width: 100%;">'
    """
    img_format = img_path.split(".")[-1]
    img_html = f'<img src="data:image/{img_format.lower()};base64,{img_to_bytes(img_path)}" alt="{img_alt}" style="max-width: 100%;">'

    return img_html


def markdown_insert_images(markdown):
    """
    Replaces image markdown with HTML image tags in a given markdown string.

    Args:
        markdown (str): The markdown string to process.

    Returns:
        str: The processed markdown string with image markdown replaced by HTML image tags.
    """
    images = markdown_images(markdown)

    for image in images:
        image_markdown = image[0]
        image_alt = image[1]
        image_path = image[2]
        if os.path.exists(image_path):
            markdown = markdown.replace(
                image_markdown, img_to_html(image_path, image_alt)
            )
    return markdown


def hide_sidebar_navigation():
    """
    Hides the sidebar navigation in the Streamlit app.

    This function adds a CSS style to hide the sidebar navigation in the Streamlit app.

    Parameters:
    None

    Returns:
    None
    """
    hide_style = """
        <style>
        /* Hide the sidebar title */
        div[data-testid="stSidebarNav"] {
            display: none;
        }
        </style>
    """
    st.markdown(hide_style, unsafe_allow_html=True)


def read_markdown_file(markdown_file):
    """
    Reads the content of a markdown file.

    Args:
        markdown_file (str): The path to the markdown file.

    Returns:
        str: The content of the markdown file.
    """
    with open(markdown_file, "r", encoding="utf-8") as file:
        content = file.read()

    content = markdown_insert_images(content)

    return content


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


########################################################################### Modelization part ###########################################################################


def preprocess_image(img_path: str, target_size: tuple) -> np.array:
    """
    Load and preprocess an image to be suitable for model prediction.

    Parameters:
    - img_path (str): The path to the image.
    - target_size (tuple): The target size of the image (height, width).

    Returns:
    - img_array (np.array): Preprocessed image array.
    """
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=target_size)
    img_array = tf.keras.preprocessing.image.img_to_array(img) / 255
    img_array = np.expand_dims(
        img_array, axis=0
    )  # Model expects batches, so expand dimensions

    return img_array


def load_trained_model(model_path: str) -> tf.keras.Model:
    """
    Load a trained Keras model from the specified path.

    Parameters:
    - model_path (str): The path to the stored Keras model file.

    Returns:
    - model: The loaded Keras model.
    """
    model = tf.keras.models.load_model(model_path)

    return model


def predict(model: tf.keras.Model, img_array: np.array) -> np.array:
    """
    Predict the class of an image using the loaded model.

    Parameters:
    - model: The loaded Keras model.
    - img_array (np.array): Preprocessed image array for prediction.

    Returns:
    - prediction: The predicted result.
    """
    prediction = model.predict(img_array)

    return prediction


def load_champ_model() -> tf.keras.Model:
    """
    Load and return a pre-trained model.

    Returns:
        tf.keras.Model: The loaded pre-trained model.
    """
    model = load_trained_model("../models/TL_180px_32b_20e_model.keras")

    return model
