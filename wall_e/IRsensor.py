# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
IRsensor1 = 4 # Broadcom pin
IRsensor2 = 17
IRsensor3 = 27

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(IRsensor1, GPIO.IN) # sensor set as input 
GPIO.setup(IRsensor2, GPIO.IN)
GPIO.setup(IRsensor3, GPIO.IN)

# PROGRAM
while True:
        A = GPIO.input(IRsensor1)
	B = GPIO.input(IRsensor2)
	C = GPIO.input(IRsensor3)
        print (C, B, A)
        time.sleep(0.1)

