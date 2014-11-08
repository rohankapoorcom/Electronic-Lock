from lock import app, socketio, modules

from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')
