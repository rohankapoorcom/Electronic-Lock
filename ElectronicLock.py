import RPi.GPIO as GPIO
from RPIO import PWM
import os

#Setup GPIO using BCM  Numbering
GPIO.setmode(GPIO.BCM)

buttonPin = 24
servoPin = 18

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
servo = PWM.Servo()

doorUnlock = 1500
doorLock = 1870
currentState = False # unlocked

def lock_unlock(state):
		if (state == False):
				servo.set_servo(servoPin, doorLock)
				servo.set_servo(servoPin, 0)
		else:
				servo.set_servo(servoPin, doorUnlocked)
		return

while True:
		GPIO.wait_for_edge(buttonPin, GPIO.FALLING)
		print("Big Red Button pressed")
		GPIO.wait_for_edge(buttonPin, GPIO.RISING)
		print("Big Red Button released")
		lock_unlock(currentState)
		if (currentState == False):
				currentState = True
		else:
				currentState = False
		os.system("wemo switch eolamp toggle")
GPIO.cleanup()
