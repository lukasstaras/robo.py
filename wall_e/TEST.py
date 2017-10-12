import curses
import RPi.GPIO as GPIO

#set GPIO numbering mode and define output pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

AIN1 = 2
AIN2 = 3
PWMA = 10
BIN1 = 23
BIN2 = 24
PWMB = 18

GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
rightmotor = GPIO.PWM(PWMA, 50)
rightmotor.start(0)
leftmotor = GPIO.PWM(PWMB, 50)
leftmotor.start(0)
try:
        while True:
            char = screen.getch()
            if char == ord('q'):
 		#Close down curses properly, inc turn echo back on!
                curses.nocbreak(); screen.keypad(0); curses.echo()
                curses.endwin()
                GPIO.cleanup()
		break
            elif char == curses.KEY_UP:
		print('Forward')
                GPIO.output(AIN1, True)
		GPIO.output(AIN2, False)
		rightmotor.ChangeDutyCycle(100)

		GPIO.output(BIN1, True)
		GPIO.output(BIN2, False)
		leftmotor.ChangeDutyCycle(100)
            elif char == curses.KEY_DOWN:
		print('Beckwards')
                GPIO.output(AIN2,True)
                GPIO.output(AIN1,False)
                rightmotor.ChangeDutyCycle(100)

		GPIO.output(BIN1, False)
		GPIO.output(BIN2, True)
		leftmotor.ChangeDutyCycle(100)
            elif char == curses.KEY_RIGHT:
		print('Right')
                GPIO.output(AIN1, True)
                GPIO.output(AIN2, False)
		rightmotor.ChangeDutyCycle(60)

		GPIO.output(BIN1, True)
		GPIO.output(BIN2, False)
		leftmotor.ChangeDutyCycle(30)
            elif char == curses.KEY_LEFT:
		print('Left')
		GPIO.output(AIN1, True)
                GPIO.output(AIN2, False)
                rightmotor.ChangeDutyCycle(30)

                GPIO.output(BIN1, True)
                GPIO.output(BIN2, False)
                leftmotor.ChangeDutyCycle(60)
            else:
                GPIO.output(PWMA, False)
		GPIO.output(PWMB, False)
		print('Press UP, DOWN, LEFT OR RIGHT')
finally:
 print('Bye')
