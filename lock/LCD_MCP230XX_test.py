#!/usr/bin/python
# Example script to show usage of MCP230xx GPIO extender to drive character LCD.

from Adafruit_CharLCD import Adafruit_CharLCD
from Adafruit_MCP230xx import MCP230XX_GPIO

from datetime import datetime
from time import sleep, strftime

bus = 0        # Note you need to change the bus number to 0 if running on a revision 1 Raspberry Pi.
address = 0x20  # I2C address of the MCP230xx chip.
gpio_count = 8  # Number of GPIOs exposed by the MCP230xx chip, should be 8 or 16 depending on chip.

# Create MCP230xx GPIO adapter.
mcp = MCP230XX_GPIO(bus, address, gpio_count)

# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=6, pins_db=[1,2,3,4], GPIO=mcp)

mcp.chip.config(5, mcp.chip.OUTPUT)

while True:
	lcd.clear()
	lcd.message("Alarm Status:\n     Armed")
	mcp.output(5, 1)
	print("on")
	sleep(5)
	lcd.clear()
	lcd.message(datetime.now().strftime('%b %d  %I:%M %p\n'))
	lcd.message("E. Edison")
	mcp.output(5, 0)
	print("off")
	sleep(50)

