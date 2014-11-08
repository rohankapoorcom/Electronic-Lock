#!/usr/bin/python
import RPi.GPIO as GPIO
from ouimeaux.environment import Environment

import os
import time
import thread

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
		os.system("./lock.py &")
	else:
		os.system("./unlock.py &")
	return

def toggle_lights():
	print "Toggling lights"
	ret = switch.basicevent.GetBinaryState()
	# SBS takes a weird dict for some reason. Invert.
	ret['BinaryState'] = str(int(not int(ret['BinaryState'])))
	switch.basicevent.SetBinaryState(**ret)

def button_pushed(channel):
	global currentState
	print "Big Red Button pressed"
	timeStarted = time.time()
	while GPIO.input(buttonPin) == 0 and time.time() - timeStarted < 0.3:
		time.sleep(0.1)
	timeEnded = time.time()
	print "Big Red Button released"

	duration = timeEnded - timeStarted
	if (duration >= 0.3):
		lock_unlock(currentState)
		currentState = not currentState
	else:
		# Handle wemo toggling
		try:
			empty_tuple = ()
			thread.start_new_thread(toggle_lights, empty_tuple)
		except:
			print "Error: unable to start thread"


GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback=button_pushed, bouncetime=2000)
while True:
	pass
	
GPIO.cleanup()
