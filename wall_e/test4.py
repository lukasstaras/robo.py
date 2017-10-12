
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

AIN1 = 2
AIN2 = 3
PWMA = 10
BIN1 = 23
BIN2 = 24
PWMB = 18

GPIO.setwarnings(False)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(PWMA, GPIO.OUT)

GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
leftmotor = GPIO.PWM(PWMA, 50)
leftmotor.start(0)
rightmotor = GPIO.PWM(PWMB, 50)
rightmotor.start(0)

#run
while True:
        A = GPIO.input(IRsensor1)
	B = GPIO.input(IRsensor2)
	C = GPIO.input(IRsensor3)
        print(A, B, C)
        time.sleep(0.001)
	if B == 1:
		GPIO.output(AIN1, GPIO.HIGH)
		GPIO.output(AIN2, GPIO.LOW)
		rightmotor.ChangeDutyCycle(60)

		GPIO.output(BIN1, GPIO.HIGH)
		GPIO.output(BIN2, GPIO.LOW)
		leftmotor.ChangeDutyCycle(60)
	elif B == 0 and A == 0 and C == 0:
		time.sleep(2)
		GPIO.output(AIN1, GPIO.LOW)
		GPIO.output(AIN2, GPIO.LOW)
		GPIO.output(BIN1, GPIO.LOW)
		GPIO.output(BIN2, GPIO.LOW)
		leftmotor.ChangeDutyCycle(0)
		rightmotor.ChangeDutyCycle(0)
	elif C == 1:
		GPIO.output(AIN1, GPIO.HIGH)
                GPIO.output(AIN2, GPIO.LOW)
                rightmotor.ChangeDutyCycle(10)

                GPIO.output(BIN1, GPIO.LOW)
                GPIO.output(BIN2, GPIO.HIGH)
                leftmotor.ChangeDutyCycle(50)
		#time.sleep(0.001)
	elif A == 1:
		GPIO.output(AIN1, GPIO.LOW)
                GPIO.output(AIN2, GPIO.HIGH)
                rightmotor.ChangeDutyCycle(50)

                GPIO.output(BIN1, GPIO.HIGH)
                GPIO.output(BIN2, GPIO.LOW)
                leftmotor.ChangeDutyCycle(10)
               # time.sleep(0.001)


