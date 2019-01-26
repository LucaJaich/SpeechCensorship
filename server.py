from flask import Flask, request
from flask_cors import CORS
import json
import pygame
from watson_developer_cloud import TextToSpeechV1, SpeechToTextV1
from werkzeug.datastructures import FileStorage
import os



app = Flask(__name__)
CORS(app)

speech_to_text = SpeechToTextV1(
	username="b6bf9c08-1c6d-4f69-9aa7-f6795920f1c3",
	password="mqk7rw8X8isy",
	url="https://stream.watsonplatform.net/speech-to-text/api"
)

def analyze_word(audio):
	os.system("rm word.wav")
		
	file = FileStorage(audio)
	file.save("word.wav")

@app.route("/audio", methods=['POST'])
def manage_request():
	analyze_word(request.files["files"])
	return json.dumps({"hola":"que onda"})

app.run()

	