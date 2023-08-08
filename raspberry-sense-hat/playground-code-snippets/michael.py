from sense_hat import SenseHat 

sense = SenseHat()

# 
sense.clear((255, 0, 255))

sense.clear()

# Show scrolling message on 8x8 matrix
sense.show_message(text_string="Hello Michael", scroll_speed=1, text_colour=[127, 255, 127])

print("Hello Michael!") 