# Text-to-Speech Conversion

This repository contains a Python script for converting text to speech using either OpenAI's or ElevenLabs' API. It will generate an audio file from the input text and play it using the `mpg123` audio player utility.

## Purpose

The purpose of this project is to provide a simple and flexible way to convert text to speech. It can be used for a variety of applications, such as creating audio books, aiding in accessibility, or developing voice assistants.

## Future

In the future, I plan to add support for more text-to-speech APIs, as well as additional features such as saving the audio to a file, and more advanced audio manipulation to support different use cases, as well as support for different audio players and real-time audio playback.

## Getting Started

- [OpenAI Text-to-Speech Guide](https://beta.openai.com/docs/guides/text-to-speech)
- [ElevenLabs Text-to-Speech Documentation](https://elevenlabs.io/docs/introduction)
- [PlayHT Text-to-Speech Documentation](https://docs.play.ht/reference/api-getting-started)

### Prerequisites

- Python 3.6 or higher
- pip
- An API key for OpenAI and/or ElevenLabs

### Installation

1. Clone the repository:

```bash
git clone https://github.com/highwayoflife/say.git
cd say
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Set your API keys as environment variables. You only need one or the other, but you can set both if you want to use both APIs.

I suggest using [direnv](https://direnv.net/) to manage your environment variables. You can create a `.envrc` file in the root of the project with the following content, or put these in your `.profile` or `.bashrc` file, alternatively, you can just run these in the terminal before running the `say.py` script:

```bash
export OPENAI_API_KEY="your-openai-api-key"
export ELEVENLABS_API_KEY="your-elevenlabs-api-key"
```

## Usage
You can run the script from the command line (Terminal, PowerShell, etc.) with the following command:

```bash
python say.py --api openai "So, today's been pretty interesting, actually. I spent the morning catching up on some reading—lots of questions about various topics like science, history, and some really creative inquiries about art. Then, I had a chat with someone who needed help planning a birthday party for their cat, which was pretty adorable. Later on, I dived into a bit of brainstorming for a user who was writing a story and needed some ideas for plot twists. Right now, I'm here, having this conversation with you. How about you? How has your day been?"
```

This will convert the text to speech using OpenAI's API and play the audio using your default audio player.
You can use the `--api` flag to specify which API to use, the currently supported values are `openai` and `elevenlabs`.
