# This program will make an LED blink randomly, eventually from 7PM - 6AM
# but more likely just for 11 hours, then sleep for 13 hours, repeat

import RPi.GPIO as GPIO	#imports gpio and shortens name
from time import sleep 	#lets pi sleep
from random import randint
GPIO.setmode(GPIO.BCM)	#could also be (GPIO.BOARD) for using pin numbers

delay = 3600*input("Delay in hours: ")
iterations = 3600*input("Running time in hours: ")
redList  = [4, 16];	# list of all the pin numbers of the red LEDs
grnList= [5, 6];	# list of all the pin numbers of the green LEDs
allList  = redList + grnList # all LED pin numbers
for element in allList:	#iterate through all LEDs
	GPIO.setup(element, GPIO.OUT) # set them to output

for element in redList: GPIO.output(element, 0)
for element in grnList: GPIO.output(element, 1)

try:
	for i in range(0,int(delay)+int(iterations)):
		if (i%1800==0):
			print_statement = 'half-hour number:'+ repr(i/1800)
			print print_statement
		if i >= delay:
			if randint(0,1): # ~50% chance of execuiting
				for element in allList:
					GPIO.output(element, not GPIO.input(element))
		sleep(1.0014)
	print "Done."

except KeyboardInterrupt:
	print " <- I 'C' what you did there."

finally:
	GPIO.cleanup()


