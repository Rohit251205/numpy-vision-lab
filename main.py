"""
==========================================================
Project : NumPy Vision Lab
Version : 1.0

Author : Rohit Prajapati

Description:
A lightweight image processing toolkit using NumPy and Pillow.
==========================================================
"""

# ==============================
# Import Libraries
# ==============================

import numpy as np
from PIL import Image

# ==============================
# Main Code
# ==============================

# Image Loading

car_img = Image.open("images/car.jpeg")

# Convert Image In Numpy Array

car_array = np.array(car_img)

# =========================================
# IMAGE INFORMATION
# =========================================

image_shape = car_array.shape
image_height = image_shape[0]
image_width = image_shape[1]
image_channels = image_shape[2]


print("Image Loaded Successfully \n")
print("Image Name :",car_img.filename)
print("Image Shape :",image_shape)
print("Image Height :",image_height)
print("Image Width :",image_width)
print("Image Channels :",image_channels)
print("Image Size :",car_array.size)
print("Image Datatype :",car_array.dtype)
print("Minimum Pixel :",np.min(car_array))
print("Maximum Pixel :",np.max(car_array))

horizontal_flip = np.fliplr(car_array)

convert_image = Image.fromarray(horizontal_flip)

convert_image.save("output/horizontal_flip_car.jpeg")