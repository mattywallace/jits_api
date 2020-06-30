from flask import Flask, jsonify

DEBUG=True 
PORT=8000


app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/test')
def get_list():
	return jsonify(['hello', 'hi', 'doink'])

if __name__ == '__main__':
	app.run(debug=DEBUG, port=PORT)