import requests
import json
import os

XI_API_KEY = os.getenv("ELEVENLABS_API_KEY")
                       
url = "https://api.elevenlabs.io/v1/voices"

# Here, headers for the HTTP request are being set up. 
# Headers provide metadata about the request. In this case, we're specifying the content type and including our API key for authentication.
headers = {
  "Accept": "application/json",
  "xi-api-key": XI_API_KEY,
  "Content-Type": "application/json"
}

# A GET request is sent to the API endpoint. The URL and the headers are passed into the request.
response = requests.get(url, headers=headers)

# The JSON response from the API is parsed using the built-in .json() method from the 'requests' library. 
# This transforms the JSON data into a Python dictionary for further processing.
data = response.json()

voice_id_to_name = {}

# A loop is created to iterate over each 'voice' in the 'voices' list from the parsed data. 
# The 'voices' list consists of dictionaries, each representing a unique voice provided by the API.
for voice in data['voices']:
  # For each 'voice', the 'name' and 'voice_id' are printed out. 
  # These keys in the voice dictionary contain values that provide information about the specific voice.
  print(f"{voice['name']}; {voice['voice_id']}")
  # Create a map of voice IDs to voice names
  voice_id_to_name[voice['voice_id']] = voice['name']

# Get voice settings for a specific voice_id:
voice_id = "z0DcTcYlLxVjFO7tr9yB"
voice_settings_url = f"https://api.elevenlabs.io/v1/voices/{voice_id}/settings"

response = requests.get(voice_settings_url, headers=headers)
voice_settings = response.json()
# Print the voice settings for the specified voice_id, and voice name:
print(f"\nVoice settings for {voice_id}: {voice_id_to_name[voice_id]}:")
print(voice_settings)