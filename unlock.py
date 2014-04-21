#!/usr/bin/python
from RPIO import PWM
import time

servoPin = 18
doorUnlock = 1560;

# Setup RPIO Servo control
servo = PWM.Servo()

# Unlock door
servo.set_servo(servoPin, doorUnlock)
time.sleep(0.5)

# Servo/lock mechanics require we stop the servo once the door has unlocked
servo.set_servo(servoPin, 0)