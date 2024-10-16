from pathlib import Path
from openai import OpenAI

import os

#define openAI client
client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input="My name is alloy and I am testing my voice right now."
)

response.stream_to_file("output.mp3")

# response.stream_to_file(speech_file_path)
# audio_file= open("/path/to/file/audio.mp3", "rb")
# transcription = client.audio.transcriptions.create(
#     model="whisper-1", 
#     file=audio_file,
#     response_format="text"
# )
# print(transcription.text)
