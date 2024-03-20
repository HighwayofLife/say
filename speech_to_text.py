from pathlib import Path
from openai import OpenAI

client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"

response = client.audio.speech.create(
  model = "tts-1-hd",
  voice = "echo",
  input = "Hello, my name is Echo Chamber. I am a text to voice application and I should sound completely human."
)

response.stream_to_file(speech_file_path)


