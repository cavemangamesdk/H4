from sense_hat import SenseHat
import numpy as np
import time

# Initialize the Sense Hat
sense = SenseHat()

R = [255, 0, 0]  # Red
G = [0, 255, 0]
B = [0, 0, 255]
W = [255, 255, 255]  # White

question_mark = [
R, R, R, R, R, B, B, B,
R, R, R, R, B, R, B, B,
R, R, R, R, B, R, B, B,
R, R, R, R, R, B, B, B,
B, B, B, R, B, B, B, B,
B, B, B, R, B, B, B, B,
B, B, B, B, B, B, B, B,
B, B, B, R, B, B, B, B
]

sense.set_pixels(question_mark)

time.sleep(3)

# Get the current image (8x8 pixels)
image = np.array(sense.get_pixels())

# Reshape the image into an 8x8 matrix
image = image.reshape((8, 8, 3))

# Create a new image for the smoothed pixels
smoothed = np.zeros_like(image)

# For each pixel
for i in range(8):
    for j in range(8):
        # Get the surrounding pixels
        surrounding = image[max(0, i-1):min(8, i+2), max(0, j-1):min(8, j+2)]
        
        # Average the colors
        smoothed[i, j] = np.mean(surrounding, axis=(0, 1))

# Reshape the smoothed image back into a list of pixels
smoothed = smoothed.reshape((-1, 3))

# Set the pixels of the Sense Hat
sense.set_pixels(smoothed.tolist())
