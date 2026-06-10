# Ashi 🎙️

AI-powered voice journal that records your day, transcribes your speech, and analyzes wins and losses using Claude AI.

## What it does
- Records your voice
- Transcribes speech using OpenAI Whisper
- Analyzes wins and losses using Anthropic Claude API
- Saves daily entries to a JSON journal

## Tech Stack
- Python
- OpenAI Whisper — speech recognition
- Anthropic Claude API — AI analysis
- sounddevice / soundfile — audio recording

## How to run

1. Clone the repo:
git clone https://github.com/marinapushkareva1312/ashi.git

2. Install dependencies:
pip install sounddevice soundfile numpy openai-whisper anthropic python-dotenv

3. Create a .env file and add your Anthropic API key:
ANTHROPIC_API_KEY=your_key_here

4. Install ffmpeg (required for Whisper):
choco install ffmpeg

5. Run:
python app.py

## Author
Marina Pushkareva