# CircuitPlaygroundExpress_NeoPixel

import board
import neopixel
import time
from digitalio import DigitalInOut, Direction, Pull


def light_up_led(color, brightness_level):
    if color == "green":
        pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=brightness_level)
        pixels.fill((0,255,0))
    elif color == "blue":
        pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=brightness_level)
        pixels.fill((0,255,255))
    time.sleep(1)
    pixels.fill((0,0,0))

button_a = DigitalInOut(board.BUTTON_A)
button_a.direction = Direction.INPUT
button_a.pull = Pull.DOWN

button_b = DigitalInOut(board.BUTTON_B)
button_b.direction = Direction.INPUT
button_b.pull = Pull.DOWN

slide_switch = DigitalInOut(board.SLIDE_SWITCH)
slide_switch.direction = Direction.INPUT
slide_switch.pull = Pull.UP



while True:
    if slide_switch.value == True:
        b_level = 0.5
    else:
        b_level = 0.1
    # b_level = 0.1
    if button_a.value == True:  # button is pushed
        light_up_led("green", b_level)

    elif button_b.value == True:
        light_up_led("blue", b_level)
    time.sleep(0.01)
