import utils
from PIL import Image

import streamlit as st


def prediction_home():
    """
    Function to perform image prediction and display results.

    Returns:
        None
    """

    st.header("Prediction 🍃")

    # model = load_champ_model()

    st.write("")
    st.subheader("Upload an image")
    st.markdown("*Note: please don't expect too much and don't load strange image.*")

    c1, _, _ = st.columns(3)
    with c1:
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


"""
if __name__ == "__main__":
    # Path to the saved model and the image
    model_path = "models/TL_180px_32b_20e_model.keras"
    # model_path = "models/lume_models.keras"
    img_path = "data/raw/Orange___Citrus_greening/image (100).jpg"

    # Load the model
    model = load_trained_model(model_path)

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
