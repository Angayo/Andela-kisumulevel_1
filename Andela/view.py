from run import app
from flask import jsonify

@app.route('/')
def index():
	return jsonify({'Message': 'Welcome to Andela Library'})
