import sounddevice as sd
import soundfile as sf
import numpy as np
import whisper
import anthropic
import json
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

def record_voice(seconds=10, filename="voice.wav"):
    print("Recording started... Speak now!")
    sample_rate = 44100
    recording = sd.rec(
        int(seconds * sample_rate),
        samplerate=sample_rate,
        channels=1
    )
    sd.wait()
    sf.write(filename, recording, sample_rate)
    print("Recording complete!")

def transcribe(filename="voice.wav"):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    return result["text"]

def analyze(text):
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": f"Extract wins and losses from this text: {text}"}
        ]
    )
    return message.content[0].text

def save_entry(text, analysis):
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "said": text,
        "analysis": analysis
    }
    try:
        with open("journal.json", "r") as f:
            data = json.load(f)
    except:
        data = []
    data.append(entry)
    with open("journal.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Entry saved!")

record_voice()
text = transcribe()
print("You said:", text)
result = analyze(text)
print("Analysis:", result)
save_entry(text, result)