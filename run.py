from lock import app, socketio
import lock

def main():
	app.debug = True
	socketio.run(app, host='0.0.0.0', port=5000)


if __name__ == '__main__':
	from gevent import monkey
	monkey.patch_all()
	main()