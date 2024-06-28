import base64
import time
import os
import re
from pathlib import Path
from typing import BinaryIO, Tuple
from PIL import Image
import numpy as np
import tensorflow as tf
import streamlit as st

# packages imported for classical model
from skimage.feature import hog
import xgboost as xgb
import cv2


class_names = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Background_without_leaves",
    "Black-grass",
    "Blueberry___healthy",
    "Charlock",
    "Cherry___Powdery_mildew",
    "Cherry___healthy",
    "Cleavers",
    "Common Chickweed",
    "Common wheat",
    "Corn___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn___Common_rust",
    "Corn___Northern_Leaf_Blight",
    "Corn___healthy",
    "Fat Hen",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Loose Silky-bent",
    "Maize",
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Scentless Mayweed",
    "Shepherds Purse",
    "Small-flowered Cranesbill",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Sugar beet",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy",
]


########################################################################### Classical Model Part ###########################################################################

def load_classical_model(model_path):
    # Load the classical machine learning model using pickle
    # Create a progress bar
    progress_bar = st.progress(0)

    # Simulate a loading process with incremental updates
    for i in range(100):
        # Update progress bar
        time.sleep(0.01)  # Simulate some aspect of loading
        progress_bar.progress(i + 1)

    try:
        model = xgb.Booster()
        model.load_model(model_path)

        # Complete the progress bar
        progress_bar.progress(100)
        progress_bar.empty()

        return model
    except ModuleNotFoundError as e:
        st.error(f"Error loading model: {e}")
        st.stop()


def classical_ml_predict(model, image):
    # Convert PIL Image to an OpenCV image
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    image = cv2.resize(image, (256, 256))
    # Extract features
    test_features = extract_hog_color_hist_features(image)
    test_features_reshaped = test_features.reshape(1, -1)
    test_features_reshaped = xgb.DMatrix(test_features_reshaped)
    # Predict with loaded model
    predicted_label = model.predict(test_features_reshaped)[0]
    indices_dict = {
        0: 'Apple___Apple_scab',
        1: 'Apple___Black_rot',
        2: 'Apple___Cedar_apple_rust',
        3: 'Apple___healthy'
    }
    predicted_class = indices_dict[predicted_label]
    
    return predicted_class

# Function to extract combined HOG and color histogram features


def extract_hog_color_hist_features(image, resize=(256, 256)):
    image = cv2.resize(image, resize)
    # Extract HOG features
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hog_features = hog(gray_image, orientations=9, pixels_per_cell=(8, 8),
                       cells_per_block=(2, 2), block_norm='L2-Hys', visualize=False)

    # Extract color histogram features
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()

    # Combine HOG and color histogram features
    combined_features = np.hstack((hog_features, hist))
    return combined_features


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
        key=True
    )

    if img_file is None:
        image_present = False
        img_file = open("web/img/no_image_plant.jpg", "rb")

    return img_file, image_present


def load_model_with_progress(model_path) -> tf.keras.Model:
    # Create a progress bar
    progress_bar = st.progress(0)

    # Simulate a loading process with incremental updates
    for i in range(100):
        # Update progress bar
        time.sleep(0.01)  # Simulate some aspect of loading
        progress_bar.progress(i + 1)

    # Load your model (assuming the model is saved in the same directory)
    model = tf.keras.models.load_model(model_path)

    # Complete the progress bar
    progress_bar.progress(100)
    progress_bar.empty()

    return model


########################################################################### Modelization part ###########################################################################


def preprocess_image(pil_image: str, data: object) -> np.array:
    """
    Load and preprocess an image to be suitable for model prediction.

    Parameters:
    - img_path (str): The path to the image.
    - target_size (tuple): The target size of the image (height, width).

    Returns:
    - image_array (np.array): Preprocessed image array.
    """
    # Convert to RGB if it's not already
    if data["color_mode"] == "RGB":
        pil_image = pil_image.convert('RGB')
    else:
        pil_image = pil_image.convert('L')

    # Resize the image
    target_size = data["target_size"]
    interpolation = Image.BILINEAR  # PIL interpolation methods

    keep_aspect_ratio = data["keep_aspect_ratio"]

    if not keep_aspect_ratio:
        resized_image = pil_image.resize(target_size, interpolation)
    else:
        # Optionally handle aspect ratio if needed (manual implementation required)
        resized_image = pil_image  # Placeholder for actual aspect ratio handling

    # Convert to a NumPy array
    image_array = np.array(resized_image)

    # Ensure the image is in the expected shape (height, width, channels)
    image_array = tf.convert_to_tensor(image_array, dtype=tf.float32)

    # Add a batch dimension if required (model expects batched input)
    image_array = tf.expand_dims(image_array, axis=0)

    return image_array


def predict(model: tf.keras.Model, image_array: np.array) -> np.array:
    """
    Predict the class of an image using the loaded model.

    Parameters:
    - model: The loaded Keras model.
    - img_array (np.array): Preprocessed image array for prediction.

    Returns:
    - prediction: The predicted result.
    """
    # prediction = model.predict(image_array)
    predicted_classes = np.array([])
    predicted_classes = np.concatenate([predicted_classes, np.argmax(
        model(image_array, training=False), axis=-1)]).astype(int)
    c_predicted_class = np.array(class_names)[predicted_classes][0]
    confidence = np.max(model(image_array, training=False), axis=-1).item()
    # c_predicted_class = f"{c_predicted_class:.2%}"
    confidence = f"{confidence:.2%}"

    return c_predicted_class, confidence
