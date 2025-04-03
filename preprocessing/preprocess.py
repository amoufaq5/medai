# preprocessing/preprocess.py
import tensorflow as tf
import re
import logging
import cv2
import numpy as np

logger = logging.getLogger(__name__)

def clean_text(text):
    # Remove non-alphanumeric characters and extra spaces
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    cleaned = text.strip().lower()
    logger.debug(f"Cleaned text: {cleaned}")
    return cleaned

def preprocess_image(image_path, target_size=(224, 224)):
    try:
        # Load image using OpenCV and resize
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Image not loaded")
        img = cv2.resize(img, target_size)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Normalize pixel values
        img = img / 255.0
        return img
    except Exception as e:
        logger.error(f"Error preprocessing image {image_path}: {e}")
        return None

def create_text_dataset(texts, labels, batch_size=32):
    # Create a TensorFlow dataset for text data
    dataset = tf.data.Dataset.from_tensor_slices((texts, labels))
    dataset = dataset.shuffle(buffer_size=1000).batch(batch_size)
    return dataset

def create_image_dataset(image_paths, labels, batch_size=32):
    # Create a TensorFlow dataset for images
    def load_and_preprocess(path, label):
        img = tf.io.read_file(path)
        img = tf.image.decode_image(img, channels=3)
        img = tf.image.resize(img, [224, 224])
        img = img / 255.0
        return img, label
    dataset = tf.data.Dataset.from_tensor_slices((image_paths, labels))
    dataset = dataset.map(load_and_preprocess).batch(batch_size)
    return dataset
vvv
