import time
import datetime
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
EchoPin = 16
TrigPin = 15
GPIO.setup(TrigPin,GPIO.OUT)
GPIO.setup(EchoPin,GPIO.IN)


def reading(sensor):
    pingtime = 0
    echotime = 0
    if sensor == 0:
        GPIO.output(TrigPin,GPIO.LOW)
        GPIO.output(TrigPin,GPIO.HIGH)
        pingtime=time.time()
        time.sleep(0.00001)
        GPIO.output(TrigPin,GPIO.LOW)
        while GPIO.input(EchoPin)==0:
            pingtime = time.time()
        while GPIO.input(EchoPin)==1:
            echotime=time.time()
        if (echotime is not None) and (pingtime is not None):
            elapsedtime = echotime - pingtime
            distance = elapsedtime * 17000
        else:
            distance = 0
        return distance

while True:
    range = reading(0)
    print'Distance is:', format(range, '.02f'), 'cm'
    time.sleep(0.25)
