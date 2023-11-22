from flask import jsonify, request, Flask, Response
from flask_cors import CORS
from pydub import AudioSegment
import base64
import os
from stream_audio import stream_audio

def process_audio():
    """Takes in the voice message from the frontend and process it"""
    try:
        #Get the audio file from the client
        audioBlob = request.files['audio']
        audio_segment = AudioSegment.from_file(audioBlob)

        # Save audio as MP3 file
        audio_path = 'uploads/audio.mp3'
        audio_segment.export(audio_path, format='mp3')
        raw_audio_data = stream_audio()
        return Response(raw_audio_data, content_type='audio/mpeg')

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

