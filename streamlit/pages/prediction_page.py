import time
import utils
from PIL import Image
import streamlit as st

# packages imported by Arif
import numpy as np
from skimage.feature import hog
import pickle
import cv2


def model_selection(model_list, selected_model):

    model_file = model_list[selected_model]
    # Code provide by Arif
    model = None
    if selected_model == "Machine Learning (XGBClassifier)":
        model = load_traditional_model("../models/" + model_file)
    else:
        model = utils.load_model_with_progress("../models/" + model_file)
    
    print('value of model')
    print(model)
    st.success(f"Model {selected_model} loaded successfully!")
    st.write("Now you can use the model for predictions or further analysis:")

    st.write("")
    st.subheader("Upload an image")
    st.markdown("*Note: please don't expect too much and don't load strange image.*")

    image, image_valid = utils.upload_image()

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
            # Code provided by Arif
            if selected_model == "Machine Learning (XGBClassifier)":
                result = traditional_ml_predict(model, image)
            else:
                result = 'Deep Learning model goes here'
            
            st.write(result)

"""
    # Preprocess the image
    img_array = preprocess_image(img_path, target_size=(180, 180))

    # Classes name
    class_names = model.class_names

    # Make a prediction
    probability = predict(model, img_array).flatten()

    # Apply a sigmoid since our model returns logits
    probability = tf.nn.sigmoid(probability)
    probability = tf.where(probability < 0.5, 0, 1)

    # Output the prediction
    print(f"Probability array: {class_names[probability[0]]}")
"""


def prediction_home():
    """
    Function to perform image prediction and display results.

    Returns:
        None
    """
    model_list = {
        "Transfer Learning": "TL_180px_32b_20e_model.keras",
        "LeNet": "Lenet_64px_32b-200e-model.keras",
        "Augmented LeNet": "AuLexNet5_128px_gray_32b_100e_model.keras",
        "Machine Learning (XGBClassifier)": "xgboost_model.pkl",
    }

    st.header("Prediction 🍃")
    st.subheader("1. Choose which model you want to use for prediction")

    csb1, _, _ = st.columns(3)
    with csb1:
        selected_model = st.selectbox('Select a model to load:', 
                                  ['Please select a model...'] + list(model_list.keys()),
                                  key="model_select_box")

        # Conditional content based on the selection
        if selected_model != 'Please select a model...':
            model_selection(model_list, selected_model)


########################### code provided by Arif ######################################

def load_traditional_model(model_path):
    # Load the traditional machine learning model using pickle
    try:
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        return model
    except ModuleNotFoundError as e:
        st.error(f"Error loading model: {e}")
        st.stop()

def traditional_ml_predict(model, image):
    # Convert PIL Image to an OpenCV image
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    image = cv2.resize(image, (256, 256))
    # Extract features
    test_features = extract_hog_color_hist_features(image)
    test_features_reshaped = test_features.reshape(1, -1)
    # Predict with loaded model
    predicted_label = model.predict(test_features_reshaped)[0]
    indices_dict = {
        0: 'Apple___Apple_scab',
        1: 'Apple___Black_rot',
        2: 'Apple___Cedar_apple_rust',
        3: 'Apple___healthy'
    }
    predicted_class = indices_dict[predicted_label]
    return f"Predicted class: {predicted_class}"


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

########################### code provided by Arif ######################################