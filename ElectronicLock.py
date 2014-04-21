#!/usr/bin/python
import RPi.GPIO as GPIO
from ouimeaux.environment import Environment
import os
import time

# Setup GPIO using BCM Numbering
GPIO.setmode(GPIO.BCM)

buttonPin = 24
currentState = False # Unlocked

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup the WeMo Environment
env = Environment()
env.start()
switch = env.get_switch('eolamp')

def lock_unlock(state):
	if not state:
		os.system("./lock.py")
	else:
		os.system("./unlock.py")
	return

while True:
	GPIO.wait_for_edge(buttonPin, GPIO.FALLING)
	timeStarted = time.time()
	print("Big Red Button pressed")
#	GPIO.wait_for_edge(buttonPin, GPIO.RISING)
	while GPIO.input(buttonPin) == 0 and time.time() - timeStarted < 0.5:
		# Wait some small amount of time.
		# time.sleep(0.01)
		pass
	timeEnded = time.time()
	print("Big Red Button released")

	duration = timeEnded - timeStarted
	if (duration >= 0.5):
		lock_unlock(currentState)
		currentState = not currentState
	else:
		# Handle wemo toggling
		ret = switch.basicevent.GetBinaryState()
		# SBS takes a weird dict for some reason. Invert.
		ret['BinaryState'] = str(int(not int(ret['BinaryState'])))
		switch.basicevent.SetBinaryState(**ret)

		time.sleep(0.01)

GPIO.cleanup()
