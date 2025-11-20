import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

class DiseaseDetectorTool:
    def __init__(self, model_path='../models/disease_model.h5'):
        self.model = tf.keras.models.load_model(model_path)
        self.img_size = (224, 224)
        # Replace with your label mapping
        self.class_labels = {0:'Apple Scab', 1:'Corn Healthy', 2:'Tomato Early Blight'}

    def preprocess_image(self, img_path):
        img = image.load_img(img_path, target_size=self.img_size)
        img_array = image.img_to_array(img)/255.0
        img_array = np.expand_dims(img_array, axis=0)
        return img_array

    def predict(self, img_path):
        img_array = self.preprocess_image(img_path)
        pred = np.argmax(self.model.predict(img_array))
        return f"Detected Disease: {self.class_labels.get(pred,'Unknown')}"
