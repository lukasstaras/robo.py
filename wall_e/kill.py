import signal, os
import RPi.GPIO as GPIO

PWMA = 10
PWMB = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(PWMA, GPIO.OUT)

GPIO.setup(PWMB, GPIO.OUT)

#run
GPIO.output(PWMA, GPIO.LOW)
GPIO.output(PWMB, GPIO.LOW)

