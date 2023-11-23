"""This is meant to stream the response back to the user."""
from flask import send_file, Response
import os
from io import BytesIO

def stream_audio():
    #place holder the mp3 from the text-to-speech ai
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) #path of this file
    UPLOADS_DIR = os.path.join(SCRIPT_DIR, 'uploads')
    mp3_file_path = os.path.join(UPLOADS_DIR, 'audio.mp3')

    #Read the MP3 file
    with open(mp3_file_path, 'rb') as mp3_file:
        binary_data = mp3_file.read()

    #Set the appropriate content type for an MP3 file
    content_type = 'audio/mpeg'

    #Convert to blob file
    bytes_io = BytesIO(binary_data)

    return bytes_io, content_type
print(stream_audio())
