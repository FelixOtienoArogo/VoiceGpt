from flask import jsonify, request, Flask, Response
from flask_cors import CORS
from pydub import AudioSegment
import base64
import os
from web_flask.stream_audio import stream_audio

def process_audio():
    """Takes in the voice message from the frontend and process it"""
    try:
        #Get the audio file from the client
        audioBlob = request.files['audio']
        audio_segment = AudioSegment.from_file(audioBlob)

        # Save audio as MP3 file
        SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) #path of this file
        UPLOADS_DIR = os.path.join(SCRIPT_DIR, 'uploads')
        os.makedirs(UPLOADS_DIR, exist_ok=True)
        audio_path = os.path.join(UPLOADS_DIR, 'audio.mp3')
        audio_segment.export(audio_path, format='mp3')
        #raw_audio_data = stream_audio()
        return jsonify({'status': 'success'})#Response(raw_audio_data, content_type='audio/mpeg')

    except Exception as e:
        print(e)
        return jsonify({'status': 'error', 'message': str(e)})

