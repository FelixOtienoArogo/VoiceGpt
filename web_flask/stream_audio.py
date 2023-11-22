"""This is meant to stream the response back to the user."""
from flask import send_file, Response
from pydub import AudioSegment
from io import BytesIO

def stream_audio():
    #place holder the mp3 from the text-to-speech ai
    mp3_file_path = 'uploads/audio.mp3'

    #Read the MP3 file into an AudioSegment
    audio_segment = AudioSegment.from_file(mp3_file_path, format='mp3')

    # Convert the AudioSegment to raw audio data
    raw_audio_data = audio_segment.raw_data

    #Set the appropriate content type for an MP3 file
    #content_type = 'audio/mpeg'

    return raw_audio_data
