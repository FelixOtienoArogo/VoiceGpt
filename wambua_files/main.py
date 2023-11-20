import os
from pathlib import Path

from openai import OpenAI
from dotenv import load_dotenv
import pygame

# Initialize pygame
pygame.init()

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

#  Step 1: get the audio from user and save to mp3, and convert audio to text.
#  This step is not complete.

# Step 2: speech to text
audio_file = open("speech.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file,
  response_format="text"
)
transcript


#  Chat Completion API
messages1 = [
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "define weather?"}
]
chat_completion_res = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    # response_format={"type": "json_object"},
    messages=messages1
)

print(f'1:{chat_completion_res.choices[0].message.content}')

#  Text to speech response API
speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=chat_completion_res.choices[0].message.content
)
response.stream_to_file(speech_file_path)

#  Read the speech.mp3 file to user in real time.


# Load the MP3 file
mp3_file_path = "speech.mp3"
pygame.mixer.music.load(mp3_file_path)

# Play the MP3 file
pygame.mixer.music.play()

# Keep the program running while the music is playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Adjust the tick value as needed

# Quit pygame
pygame.quit()
