import os
from openai import OpenAI
from sys import argv
import subprocess
import requests 
import argparse

def create_output_directory():
    """
    Creates an output directory if it doesn't already exist.
    """
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def get_next_filename(output_dir):
    """
    Determines the next available filename in the output directory.
    
    Parameters:
    - output_dir: The directory where output files are saved.

    Returns:
    - A string with the path for the next output file.
    """
    files = [file for file in os.listdir(output_dir) if file.endswith(".mp3")]
    if not files:
        return os.path.join(output_dir, "speech_1.mp3")
    else:
        highest_num = max([int(file.split("_")[-1].split(".")[0]) for file in files])
        return os.path.join(output_dir, f"speech_{highest_num + 1}.mp3")

def openai_text_to_speech(input_text, output_dir="output", model="tts-1-hd", voice="fable"):
    """
    Converts text to speech using OpenAI's API and saves it to a file.

    Parameters:
    - input_text: The input text to convert to speech.
    - output_dir: The directory to save the output file.
    - model: The OpenAI TTS model to use.
    - voice: The voice model to use.

    Returns:
    - The path to the created audio file.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable not found.")

    client = OpenAI(api_key=api_key)
    
    # Determine the output filename
    output_file = get_next_filename(output_dir)
    
    response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=input_text
    )

    # Assuming response.write_to_file is a method that exists and writes to the specified path
    response.write_to_file(output_file)

    return output_file

def elevenlabs_text_to_speech(input_text, output_dir="output", voice_id="z0DcTcYlLxVjFO7tr9yB", model_id="eleven_turbo_v2", voice_settings={ "stability": 0.5, "similarity_boost": 0.75, "style": 0.0, "use_speaker_boost": True }):
    """
    Converts text to speech using Eleven Labs' API and saves it to a file.

    Parameters:
    - input_text: The input text to convert to speech.
    - output_dir: The directory to save the output file.
    - voice_id: The voice model to use.
    - model_id: The model to use.
    - voice_settings: The voice settings to use:
        - stability: A float between 0.0 and 1.0 that controls how much the voice should change over time.
        - similarity_boost: A float between 0.0 and 1.0 that controls how much the voice should change based on the input text.
        - style: A float between 0.0 and 1.0 that controls how much the voice should change based on the style of the input text.
        - use_speaker_boost: A boolean that controls whether the voice should be adjusted to sound more like the speaker.

    Returns:
    - The path to the created audio file.
    """
    chunk_size = 1024
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        raise EnvironmentError("ELEVENLABS_API_KEY environment variable not found.")
      
    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"

    headers = {
        "Accept": "application/json",
        "xi-api-key": api_key
    }

    data = {
        "text": input_text,
        "model_id": model_id,
        "voice_settings": voice_settings    
    }

    response = requests.post(tts_url, headers=headers, json=data, stream=True)

    if response.ok:
        output_file = get_next_filename(output_dir)
        with open(output_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                f.write(chunk)
        return output_file
    else:
        raise Exception(f"An error occurred: {response.text}")

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Convert text to speech.')
  parser.add_argument('text', help='The text to convert to speech.')
  parser.add_argument('--api', choices=['openai', 'elevenlabs'], default='elevenlabs', help='The API provider to use for text-to-speech conversion.')
#   parser.add_argument('--voice', help='The voice model to use for text-to-speech conversion.')
  args = parser.parse_args()

  try:
    # Ensure the output directory exists
    output_dir = create_output_directory()
    # Generate the speech file
    if args.api == 'openai':
      audio_file = openai_text_to_speech(args.text, output_dir)
    elif args.api == 'elevenlabs':
      audio_file = elevenlabs_text_to_speech(args.text, output_dir)
    # Play the audio file
    subprocess.run(['mpg123', audio_file])
    print("Audio content played successfully.")
  except Exception as e:
    print(f"An error occurred: {e}")
