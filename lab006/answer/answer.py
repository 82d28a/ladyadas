import time
import board
import adafruit_lis3dh
import busio

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)
lis3dh.range = adafruit_lis3dh.RANGE_8_G


while True:
    x, y, z = lis3dh.acceleration
    print((x, y, z))
    if x > 1.0 or x < 0.01: 
        print("beep")
        # you would play sound or light up colors here.
    elif y > 1.0 or y < -0.2:
        print("bop")
        # you would play sound or light up colors here.
    elif z > 10 or z < 8.0:
        print("aaah")
        # you would play sound or light up colors here.
    time.sleep(1)
