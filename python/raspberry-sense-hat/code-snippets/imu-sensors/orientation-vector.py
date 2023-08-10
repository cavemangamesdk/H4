from sense_hat import SenseHat
import time
import math

sense = SenseHat()

def calculate_direction_vector(pitch, yaw):
    x = math.cos(yaw) * math.cos(pitch)
    y = math.sin(yaw) * math.cos(pitch)
    z = math.sin(pitch)
    return x, y, z

def apply_roll(direction_vector, roll):
    roll_matrix = [
        [1, 0, 0],
        [0, math.cos(roll), -math.sin(roll)],
        [0, math.sin(roll), math.cos(roll)]
    ]
    x, y, z = direction_vector
    new_x = roll_matrix[0][0] * x + roll_matrix[0][1] * y + roll_matrix[0][2] * z
    new_y = roll_matrix[1][0] * x + roll_matrix[1][1] * y + roll_matrix[1][2] * z
    new_z = roll_matrix[2][0] * x + roll_matrix[2][1] * y + roll_matrix[2][2] * z
    return new_x, new_y, new_z

def normalize_vector(vector):
    magnitude = math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
    normalized_vector = [component / magnitude for component in vector]
    return normalized_vector

while True:

    orientation_radians = sense.get_orientation_radians()

    roll= orientation_radians['roll']
    pitch = orientation_radians['pitch']
    yaw  = orientation_radians['yaw']

    # Calculate the direction vector
    direction_vector = calculate_direction_vector(pitch, yaw)

    # Apply roll if needed
    direction_vector = apply_roll(direction_vector, roll)

    # Normalize the vector to make it a unit vector
    unit_vector = normalize_vector(direction_vector)

    print("Unit Vector:", unit_vector)