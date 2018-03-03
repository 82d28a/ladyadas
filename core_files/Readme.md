Latest Release of CircuitPython:

https://github.com/adafruit/circuitpython/releases/latest
Choose the file that starts with "adafruit-circuitpython-circuitplayground_express-#.#.#.uf2"
Unzip the file.

Reflashing/Upgrade steps:
1. Set CPE in flash mode by clicking the reset button 2 times (double clicking).
2. You will see all 10 neopixils light up green and then see a new USB drive mounted called "CPLAYBOOT".
3. Copy the file above to the USB drive.
4. If done properly you will see CPE reboot and CIRCUITPY USB drive mount instead.
5. Don't worry, all your previous code will still be there.


Latest CircuitPython Libraries aka "lib" folder:

https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/latest
Choose the file that starts with "adafruit-circuitpython-bundle-#.#.#-mpy-#######.zip"
Unzip the file.

Updating or adding Python Libraries:
* If you have an older "lib" folder in the CIRCUITPY USB drive delete it.
1. Copy the "lib" folder and all contents to the CIRCUITPY USB drive.
2. Your device may reboot. I suggest ejecting the CPE and the reconnecting the CPE.

To confirm everthing is working try running your previous code or one of the example code.