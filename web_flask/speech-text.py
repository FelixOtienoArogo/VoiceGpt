import whisper

model = whisper.load_model("base")
transcript = model.transcribe("Test1.mp3")

print(transcript['text'])
