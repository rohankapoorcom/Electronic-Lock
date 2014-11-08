#!/usr/bin/python
 
from lock.Adafruit_MCP230xx import Adafruit_MCP230XX

import time

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
		time.sleep(seconds)
		self.GPIO.output(self.pin, False)

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
