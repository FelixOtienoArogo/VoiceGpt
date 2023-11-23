from flask import jsonify, request, Flask, Response, send_file
from flask_cors import CORS
from pydub import AudioSegment
import os
from web_flask.stream_audio import stream_audio
from web_flask.speech_text import speech_text
from web_flask.text_speech import text_speech
from web_flask.chat_completion import chat_completion

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

        #Convert the audio to text
        search_text = speech_text(audio_path)
        print(search_text)

        #Accessing chatGPT for a response
        reply_text = chat_completion(search_text)
        print(reply_text)

        #Convert the reply to speech
        audioReply = text_speech(reply_text)


        #Getting raw audio data to send back
        bytes_io, content_type = stream_audio(audioReply)
        return Response(bytes_io, content_type=content_type)

    except Exception as e:
        print(e)
        return jsonify({'status': 'error', 'message': str(e)})

