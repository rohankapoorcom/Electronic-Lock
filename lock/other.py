#!/usr/bin/python

from RPIO import PWM 

from lock.Adafruit_MCP230xx import Adafruit_MCP230XX

from gevent import sleep

class Buzzer:
	
	def __init__(self, pin, GPIO=None):
		if not GPIO:
			import RPi.GPIO as GPIO
			GPIO.setwarnings(False)
		self.GPIO = GPIO
		self.GPIO.setmode(GPIO.BCM)
		self.pin = pin
		self.GPIO.setup(self.pin, GPIO.OUT)

	def buzz(self, seconds):
		self.GPIO.output(self.pin, True)
		sleep(seconds)
		self.GPIO.output(self.pin, False)
		sleep(0.05)

class LED:

	def __init__(self, pin, GPIO=None):
		if not GPIO:
			import RPi.GPIO as GPIO
			GPIO.setwarnings(False)
		self.GPIO = GPIO
		self.GPIO.setmode(GPIO.BCM)
		self.pin = pin
		self.GPIO.setup(self.pin, GPIO.OUT)

	def on(self):
		self.GPIO.output(self.pin, True)

	def off(self):
		self.GPIO.output(self.pin, False)

class Lock:
	LOCKED = 1870
	UNLOCKED = 1560

	def __init__(self, pin):
		self.pin = pin
		self.servo = PWM.Servo()
		self.status = None

	def lock(self):
		self.servo.set_servo(self.pin, Lock.LOCKED)
		sleep(0.5)
		self.servo.stop_servo(self.pin)
		self.status = True

	def unlock(self):
		self.servo.set_servo(self.pin, Lock.UNLOCKED)
		sleep(0.5)
		self.servo.stop_servo(self.pin)
		self.status = False

	def get_status(self):
		return self.status
