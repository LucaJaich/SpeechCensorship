from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/audio", methods=['POST'])
def manage_request():
	dataType = request.form['dataType']

	if dataType == "word":
		analyze_word()

	elif dataType == "sentence":
		analyze_sentence()