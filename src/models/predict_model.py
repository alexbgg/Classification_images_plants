import numpy as np
import tensorflow as tf


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
    img_array = tf.keras.preprocessing.image.img_to_array(img)/255
    img_array = np.expand_dims(
        img_array, axis=0
    )  # Model expects batches, so expand dimensions

    return img_array


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
