# This program will make an LED blink randomly, eventually from 7PM - 6AM
# but more likely just for 11 hours, then sleep for 13 hours, repeat

impport RPi.GPIO as GPIO #imports gpio and shortens name
from time import sleep   #lets pi sleep
from random import randint
GPIO.setmode(GPIO.BCM)  #could also be (GPIO.BOARD) for using pin numbers

delay = 3600*input("Delay in hours: ")
iterations = 3600*input("Running time in hours: ")
GPIO.setup(4 , GPIO.OUT) #sets pin 4 as GPIO output
GPIO.setup(16, GPIO.OUT) #sets pin 16 as GPIO output

GPIO.output(4,0)
GPIO.output(16,0)

try:
	for i in range(0,int(delay)+int(iterations)):
		if(i%1800==0) & (i>1):
			print_statement = 'Half-hour:'+ repr(i/1800)
			print print_statement
		if i >= delay:
			if randint(0,1): # ~50% chance of execuiting
				GPIO.OUTPUT(4, not GPIO.input(4))#invert
				GPIO.output(16, not GPIO.input(16))
		sleep(.0997)
	print "Done."

except KeyboardInterrupt:
	print " <- I 'C' what you did there."

finally:
	GPIO.cleanup()
