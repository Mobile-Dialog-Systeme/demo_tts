import torch
from TTS.api import TTS



def main():
    # Get device
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # List available 🐸TTS models
    print(TTS().list_models())

    # Initialize TTS
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    # List speakers
    print(tts.speakers)
    print("Hello, Coqui TTS!")
    tts.tts_to_file(
    text="Hello world!  Oha it really speaks.   Was soll ich sagen?",
    speaker="Craig Gutsy",
    language="en",
    file_path="output.wav"
    )



if __name__ == "__main__":
    main()