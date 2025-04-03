# training/model.py
import tensorflow as tf
from tensorflow.keras import layers, models

def build_multimodal_model(text_vocab_size=10000, text_maxlen=100, image_input_shape=(224, 224, 3)):
    # Text branch
    text_input = layers.Input(shape=(text_maxlen,), name="text_input")
    embedding = layers.Embedding(input_dim=text_vocab_size, output_dim=128)(text_input)
    lstm = layers.LSTM(64)(embedding)
    
    # Image branch
    image_input = layers.Input(shape=image_input_shape, name="image_input")
    x = layers.Conv2D(32, (3,3), activation='relu')(image_input)
    x = layers.MaxPooling2D((2,2))(x)
    x = layers.Conv2D(64, (3,3), activation='relu')(x)
    x = layers.MaxPooling2D((2,2))(x)
    x = layers.Flatten()(x)
    image_features = layers.Dense(64, activation='relu')(x)
    
    # Combine both branches
    combined = layers.concatenate([lstm, image_features])
    dense1 = layers.Dense(64, activation='relu')(combined)
    output = layers.Dense(1, activation='sigmoid', name="output")(dense1)
    
    model = models.Model(inputs=[text_input, image_input], outputs=output)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

if __name__ == "__main__":
    model = build_multimodal_model()
    model.summary()
