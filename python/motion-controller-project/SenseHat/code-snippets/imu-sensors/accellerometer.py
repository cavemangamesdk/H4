from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
	acceleration = sense.get_accelerometer()

	acceleration_raw = sense.get_accelerometer_raw()

	# print(acceleration)
	# print(acceleration_raw)

	roll = acceleration['roll']
	pitch = acceleration['pitch']
	yaw  = acceleration['yaw']

	x_raw = acceleration_raw['x'] 
	y_raw  = acceleration_raw['y']
	z_raw  = acceleration_raw['z']

	roll = round(roll, 2)
	pitch = round(pitch, 2)
	yaw = round(yaw, 2)

	x_raw = round(x_raw, 2)
	y_raw = round(y_raw, 2)
	z_raw = round(z_raw, 2)

	print("roll={0}, pitch={1}, yaw={2}".format(roll, pitch , yaw))
	print("x={0}, y={1}, z={2}".format(x_raw, y_raw, z_raw))

	time.sleep(1)