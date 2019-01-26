from flask import Flask, request
from flask_cors import CORS
import json
from watson_developer_cloud import TextToSpeechV1, SpeechToTextV1
from werkzeug.datastructures import FileStorage
import os
from SimpleAudioIndexer import SimpleAudioIndexer as sai


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

def analyze_sentence(audio):
	'''
	os.system("rm sentence/*")
		
	file = FileStorage(audio)
	file.save("sentence/sentence.wav")
	'''
	indexer = sai(mode="ibm", src_dir="sentence", username_ibm="b6bf9c08-1c6d-4f69-9aa7-f6795920f1c3", password_ibm="mqk7rw8X8isy")
	#indexer.index_audio(basename="sentence.wav", model="es-ES_NarrowbandModel")
	indexer.index_audio(basename="sentence.wav")
	indexer.save_indexed_audio("{}/indexed_audio".format(indexer.src_dir))
	print(indexer.get_timestamps())

@app.route("/audio", methods=['POST'])
def manage_request():
	if request.form["dataType"] == "word":
		analyze_word(request.files["files"])

	elif request.form["dataType"] == "sentence":
		analyze_sentence(request.files["files"])

	return json.dumps({"hola":"que onda"})

app.run()

	