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
print("\n======================================")
print("CROP OPERATION")
print("========================================")
print("Status       : Success")
print("Image Saved  : output/crop_car.jpeg")
print("========================================")


# ==========================================
# Grayscale Transformation
# ==========================================

# Perform Grayscale Transformation using NumPy
grayscale_array = np.average(car_array, axis=2)
grayscale_array = grayscale_array.astype(np.uint8)

# Convert NumPy array back to Image
grayscale_image = Image.fromarray(grayscale_array)

# Save Grayscale image
grayscale_image.save("output/grayscale_car.jpeg")

# Success Message
print("\n======================================")
print("GRAYSCALE TRANSFORMATION")
print("========================================")
print("Status       : Success")
print("Image Saved  : output/grayscale_car.jpeg")
print("========================================")


# ==========================================
# Negative Transformation
# ==========================================

# Perform Negative Transformation using NumPy
negative_array = 255 - car_array

# Convert NumPy array back to Image
negative_image = Image.fromarray(negative_array)

# Save Negative image
negative_image.save("output/negative_car.jpeg")

# Success Message
print("\n======================================")
print("NEGATIVE TRANSFORMATION")
print("========================================")
print("Status       : Success")
print("Image Saved  : output/negative_car.jpeg")
print("========================================")


# ==========================================
# Brightness Adjustment
# ==========================================

# Brightness Value
brightness = 40

# Convert uint8 to int16 to avoid overflow
brightness_array = car_array.astype(np.int16)

# Increase Brightness
brightness_array = brightness_array + brightness

# Keep pixel values between 0 and 255
brightness_array = np.clip(brightness_array, 0, 255)

# Convert back to uint8
brightness_array = brightness_array.astype(np.uint8)

# Convert NumPy array back to Image
brightness_image = Image.fromarray(brightness_array)

# Save Brightness Image
brightness_image.save("output/brightness_car.jpeg")

# Success Message
print("\n======================================")
print("BRIGHTNESS ADJUSTMENT")
print("========================================")
print(f"Brightness Value : +{brightness}")
print("Status           : Success")
print("Image Saved      : output/brightness_car.jpeg")
print("========================================")


# ==========================================
# Image Statistics
# ==========================================

min_pixel = np.min(car_array)
print("Minimum Pixel Value :",min_pixel)

max_pixel = np.max(car_array)
print("Maximum Pixel Value :",max_pixel)

mean_pixel = np.mean(car_array)
print("Mean Pixel Value :",mean_pixel)

median_pixel = np.median(car_array)
print("Median Pixel Value :",median_pixel)

standard_deviation = np.std(car_array)
print("Standard Deviation :",standard_deviation)

variance = np.var(car_array)
print("Variance :",variance)