# image_operations.py

import io
from PIL import Image
import os
import matplotlib.pyplot as plt

def read_image(file_path):
    with open(file_path, "rb") as f:
        return f.read()

def display_image(image_data):
    image = Image.open(io.BytesIO(image_data))
    plt.imshow(image)
    plt.axis('off')  # Hide axes
    plt.show()

def list_image_files(directory):
    supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.lower().endswith(supported_formats)]
