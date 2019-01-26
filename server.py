from flask import Flask, request
from flask_cors import CORS
import json
import pygame
from watson_developer_cloud import TextToSpeechV1, SpeechToTextV1
from werkzeug.datastructures import FileStorage
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence



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
	os.system("rm sentence/*")
		
	file = FileStorage(audio)
	file.save("sentence/sentence.wav")

	sound_file = AudioSegment.from_file("sentence/sentence.wav")
	audio_chunks = split_on_silence(sound_file, 
    # must be silent for at least half a second
    min_silence_len=100,

    # consider it silent if quieter than -16 dBFS
    silence_thresh=-10
	)

	print("words: ", len(audio_chunks))
	for i, chunk in enumerate(audio_chunks):

	    out_file = "sentence/chunk{0}.wav".format(i)
	    print("exporting", out_file)
	    chunk.export(out_file, format="wav")

@app.route("/audio", methods=['POST'])
def manage_request():
	if request.form["dataType"] == "word":
		analyze_word(request.files["files"])

	elif request.form["dataType"] == "sentence":
		analyze_sentence(request.files["files"])

	return json.dumps({"hola":"que onda"})

app.run()

	