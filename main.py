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


# ==========================================
# Horizontal Flip Operation
# ==========================================

# Perform horizontal flip using NumPy
horizontal_flip_array = np.fliplr(car_array)

# Convert NumPy array back to Image
horizontal_flip_image = Image.fromarray(horizontal_flip_array)

# Save flipped image
horizontal_flip_image.save("output/horizontal_flip_car.jpeg")

# Success Message
print("\n======================================")
print("HORIZONTAL FLIP OPERATION")
print("========================================")
print("Status       : Success")
print("Image Saved  : output/horizontal_flip_car.jpeg")
print("========================================")


# ==========================================
# Vertical Flip Operation
# ==========================================

# Perform Vertical flip using NumPy
vertical_flip_array = car_array[::-1, :, :]

# Convert NumPy array back to Image
vertical_flip_image = Image.fromarray(vertical_flip_array)

# Save flipped image
vertical_flip_image.save("output/vertical_flip_car.jpeg")

# Success Message
print("\n======================================")
print("VERTICAL FLIP OPERATION")
print("========================================")
print("Status       : Success")
print("Image Saved  : output/vertical_flip_car.jpeg")
print("========================================")


# ==========================================
# Rotate 90° Operation
# ==========================================

# Perform Rotate 90° using NumPy
rotate_90_array = np.rot90(car_array)

# Convert NumPy array back to Image
rotate_90_image = Image.fromarray(rotate_90_array)

# Save Rotate 90° image
rotate_90_image.save("output/rotate_90_car.jpeg")

# Success Message
print("\n======================================")
print("ROTATE 90 OPERATION")
print("========================================")
print("Status       : Success")
print("Image Saved  : output/rotate_90_car.jpeg")
print("========================================")


# ==========================================
# Crop Operation
# ==========================================

# Calculate crop size (50% of original image)
crop_height = image_height // 2
crop_width = image_width // 2

# Calculate center crop coordinates
start_row = (image_height - crop_height) // 2
end_row = start_row + crop_height

start_column = (image_width - crop_width) // 2
end_column = start_column + crop_width

# Crop image using NumPy slicing
crop_array = car_array[
    start_row:end_row,
    start_column:end_column,
    :
]

# Convert NumPy array back to Image
crop_image = Image.fromarray(crop_array)

# Save cropped image
crop_image.save("output/crop_car.jpeg")

# Success Message
print("\n========================================")
print("CROP OPERATION")
print("========================================")
print("Status       : Success")
print("Image Saved  : output/crop_car.jpeg")
print("========================================")