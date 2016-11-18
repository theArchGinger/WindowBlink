# WindowBlink
This is a project of mine, the purpose of which is to blink some LEDs in my window, so it doesn't look lame. Anyone that lives in a large apartment building and gets free elecricity has no excuse not to do something creative with their window.

The code will be completely in python for the time being, as this is my only excuse to write python code. This code was developed and run on a RaspberryPi 2 B+.

Currently, the program will ask for an initial delay in hours before blinking should start and for a duration also in hours. The program then has a ~50% chance every second of toggling wether the Leds are on. This is done using randint from random and sleep from time. There are 2 red LEDs that are connected to pins 4 and 16 by BCM numbering.

This program can be run by the command:
	sudo python windowBlinnk.py
This assumes a GNU/Linux distro, root access, and python with time and random libraries
