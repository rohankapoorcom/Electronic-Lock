from lock import socketio, modules

from flask_socketio import emit

@socketio.on('connect')
def send_current_lcd_text():
	emit('last_message', {'data': modules['lcd'].get_last_message()})

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
