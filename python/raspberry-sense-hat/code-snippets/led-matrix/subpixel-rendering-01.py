from sense_hat import SenseHat
import numpy as np

# Initialize the Sense Hat
sense = SenseHat()

def set_pixel_frac(x, y, r, g, b):
    """Set a pixel with fractional position (x, y) to the color (r, g, b)."""
    # Calculate the weights for the neighboring pixels
    x1, x_frac = divmod(x, 1)
    y1, y_frac = divmod(y, 1)
    x1, y1 = int(x1), int(y1)
    weights = [(1 - x_frac) * (1 - y_frac), x_frac * (1 - y_frac), (1 - x_frac) * y_frac, x_frac * y_frac]

    # Calculate the colors for the neighboring pixels
    colors = [sense.get_pixel(x1 + dx, y1 + dy) for dx, dy in [(0, 0), (1, 0), (0, 1), (1, 1)]]
    colors = [[int(c + w * color) for c, color in zip(cs, (r, g, b))] for w, cs in zip(weights, colors)]

    # Set the colors of the neighboring pixels
    for (dx, dy), color in zip([(0, 0), (1, 0), (0, 1), (1, 1)], colors):
        sense.set_pixel(x1 + dx, y1 + dy, color)

# Test the function
set_pixel_frac(4.8, 4.8, 255, 0, 0)
