from sense_hat import SenseHat

sense = SenseHat()

while True:
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']

	x=round(x, 2)
	y=round(y, 2)
	z=round(z, 2)

	print("x={0}, y={1}, z={2}".format(x, y, z))