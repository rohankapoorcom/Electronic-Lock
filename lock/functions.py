from lock import socketio, modules

from flask_socketio import emit
from gevent import sleep

@socketio.on('connect')
def send_current_lcd_text():
	emit('last_message', {'data': modules['lcd'].get_last_message()})
	emit('last_locked', {'data': modules['lock'].get_status()})

@socketio.on('lcd_text')
def change_lcd_text(data):
	text = data.get('data', '')
	lines = text.strip().split('\n')
	if len(lines) > 2:
		emit('lcd_text', {'data': False})
		return
	for line in lines:
		if len(line) > 16:
			emit('lcd_text', {'data': False})
			return
	modules['lcd'].clear()
	modules['lcd'].message('\n'.join(lines))
	emit('lcd_text', {'data': True})
	emit('last_message', {'data': modules['lcd'].get_last_message()}, broadcast=True)

@socketio.on('lock')
def lock_unlock_door(msg):
	if msg['data']:
		modules['buzzer'].buzz(0.4)
		modules['lock'].lock()
	else:
		modules['buzzer'].buzz(0.15)
		modules['buzzer'].buzz(0.15)
		modules['buzzer'].buzz(0.15)
		modules['lock'].unlock()
	emit('lock', {'data': msg['data']})
	emit('last_locked', {'data': modules['lock'].get_status()}, broadcast=True)
	origin_message = modules['lcd'].get_last_message()
	modules['lcd'].clear()
	modules['lcd'].message('{}\nSUCCESSFULLY'.format('LOCKED' if msg['data'] else 'UNLOCKED'))
	sleep(0.5)
	modules['lcd'].clear()
	modules['lcd'].message(origin_message)
	modules['led'].on() if msg['data'] else modules['led'].off()