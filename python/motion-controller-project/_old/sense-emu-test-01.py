from sense_emu import SenseHat

sense = SenseHat()

temp = sense.get_temperature()
humidity = sense.get_humidity()
pressure = sense.get_pressure()

print("Temperature: %s C" % temp)
print("Humidity: %s %%rH" % humidity)
print("Pressure: %s Millibars" % pressure)
