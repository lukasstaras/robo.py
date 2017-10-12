import signal, os
import RPi.GPIO as GPIO
import time

AIN1 = 2
AIN2 = 3
PWMA = 17
BIN1 = 23
BIN2 = 24
PWMB = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(PWMA, GPIO.OUT)

GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)

#run
GPIO.output(AIN1, GPIO.HIGH)
GPIO.output(AIN2, GPIO.LOW)
GPIO.output(PWMA, GPIO.HIGH)

GPIO.output(BIN1, GPIO.HIGH)
GPIO.output(BIN2, GPIO.LOW)
GPIO.output(PWMB, GPIO.HIGH)
time.sleep(2)

GPIO.output(AIN1, GPIO.LOW)
GPIO.output(AIN2, GPIO.LOW)
GPIO.output(BIN1, GPIO.LOW)
GPIO.output(BIN2, GPIO.LOW)

