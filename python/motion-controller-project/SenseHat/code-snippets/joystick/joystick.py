# https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/9
from sense_hat import SenseHat
sense = SenseHat()


while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)