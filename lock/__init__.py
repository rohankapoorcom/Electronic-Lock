from flask import Flask
from flask_util_js import FlaskUtilJs
from flask_socketio import SocketIO

from lock.keypad import keypad
from lock.Adafruit_MCP230xx import MCP230XX_GPIO
from lock.Adafruit_CharLCD import Adafruit_CharLCD
from lock.other import Buzzer, LED

app = Flask(__name__)
fujs = FlaskUtilJs(app)
socketio = SocketIO(app)
modules = {}

modules['keypad'] = keypad(address = 0x24, num_gpios = 8, columnCount = 4)
modules['mcp'] = MCP230XX_GPIO(0, 0x20, 8)
modules['lcd'] = Adafruit_CharLCD(pin_rs=0, pin_e=6, pins_db=[1,2,3,4], GPIO=modules['mcp'])
modules['buzzer'] = Buzzer(7, GPIO=modules['mcp'])
modules['led'] = LED(5, GPIO=modules['mcp'])

import lock.views
import lock.functions
