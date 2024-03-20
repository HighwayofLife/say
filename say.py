import os
from openai import OpenAI
from sys import argv
import io
import pygame  # Import the pygame library
import subprocess


def text_to_speech(input, output_file="speech.mp3", model="tts-1-hd", voice="echo"):
    """
    Converts text to speech using OpenAI's API.

    Parameters:
    - text: The input text to convert to speech.
    - model: The OpenAI TTS model to use.

    Returns:
    - The audio content as bytes.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable not found.")

    client = OpenAI()

    client.api_key = api_key

    response = client.audio.speech.create(
        model = model,
        voice = voice,
        input = input
    )

    response.write_to_file(output_file)

    return output_file

def play_audio(audio_content):
    """
    Plays audio content using pygame.

    Parameters:
    - audio_content: The audio content to play as bytes.
    """
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the audio content
    audio_file = io.BytesIO(audio_content)
    pygame.mixer.music.load(audio_file)

    # Play the audio
    pygame.mixer.music.play()

    # Keep the script running until the audio has finished playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python say.py '<text_to_speak>'")
    else:
        text = argv[1]
        try:
            audio_file = text_to_speech(text)
            # play_audio(audio_content)
            # for playing note.wav file
            subprocess.run(['mpg123', audio_file])
            print("Audio content played successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
