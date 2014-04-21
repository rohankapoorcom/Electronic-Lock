#!/usr/bin/python
from RPIO import PWM
import time

servoPin = 18
doorLock = 1870;

# Setup RPIO Servo control
servo = PWM.Servo()

# Lock door
servo.set_servo(servoPin, doorLock)
time.sleep(0.5)

# Servo/lock mechanics require we stop the servo once the door has locked
servo.set_servo(servoPin, 0)