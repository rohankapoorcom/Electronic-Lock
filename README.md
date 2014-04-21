# ElectronicLock
Electronic Lock is a Raspberry Pi controlled door locking mechanism and lighting control system.

## Hardware
* Raspberry Pi Model B
* MCP23008 i2c i/o port expander (Raspberry Pi doesn't have nearly enough GPIOs)
* HS-311 Standard Servo Motor
* Hitachi HD44780 compatible 16x2 LCD with LED backlighting
* 10K potentiometer (for contrast adjustment on the LCD Display)
* Piezo Transducer/PC Speaker/Small Buzzer
* Grayhill 4x4 keypad
* Emergency Stop Button (for lighting/lock control on the inside of the door)
	* hereafter known as the the Big Red Button (or BRB for short)
* Belkin Wemo Switch

## Features
* A short press of the Big Red Button toggles the Wemo Switch, changing the state of the four desk lamsp connected to it (Implemented)
* A long press of the Big Red Button (1.5 seconds) triggers the lock_unlock function which toggles the state of the door lock through the servo motor (Implemented)
* Correct Entry of a user supplied pin on the externally mounted keypad triggers the lock_unlock function
	* Each user should have the option to have their own pin
	* The buzzer provides auditory feedback to the user based on keypad input
	* The keypad allows a non-approved user to ring a "doorbell" requesting access
* The externally mounted LCD screen provides visual feedback to the user
* The servo provides it's current state back to Raspberry Pi for a true closed-loop system
* Web-interface allows users to check the status of the door and lights as well as change the unlock pin
* Controllable by Tasker for Android
* Able to restart without user input

## Requirements/Dependencies
* Raspbian (for the init scripts)
* Python 2
* [ouimeaux](https://github.com/iancmcc/ouimeaux) - for controlling Belkin Wemo Devices

## Usage
**This is pre-alpha software. It is highly advised to not install/operate on a production system**
* Software installation instructions will come alongside the hardware setup guide soon

## License

Copyright (c) 2014 [Rohan Kapoor](http://rohankapoor.com) and Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
