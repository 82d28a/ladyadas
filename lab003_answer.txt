# CircuitPlaygroundExpress_Temperature
# reads the on-board temperature sensor and prints the value

import adafruit_thermistor
import board
import neopixel
import time
 
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0,0,0))
pixels.show()

thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)

while True:
    F = thermistor.temperature*9/5+32
    if F > 80.0:
        pixels.fill((255,0,0))
    elif F < 80.0:
        pixels.fill((0,255,0))
    time.sleep(0.25)

