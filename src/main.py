import torch


import pyaudio
import threading
import numpy as np
from TTS.api import TTS
import sounddevice as sd



def main():
    # Get device
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # List available 🐸TTS models
    # print(TTS().list_models())
    print("Loading 🐸 TTS model...")
    # original model
    tts1 = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=True)
    # option 1
    tts2 = TTS(model_name="tts_models/de/thorsten/tacotron2-DCA", progress_bar=True)
    # option 2
    tts3 = TTS(model_name="tts_models/de/thorsten/vits", progress_bar=True)

    print("🐸 TTS model loaded!")

    text = "Oha, das ist ja cool!  Kann ich dir helfen, oder hast du Fragen zu mir? Hier sind Aussagen von unserem Eaasy Roboter, der übrigens Pakete rakete heißt: .  Ich folge dir,. Fahrzeut steht, . Meine Bremsen sind aktiviert.  Ich sehe ein Hindernis !"
    tts_options = [tts1,tts2,  tts3]
    for tts in tts_options:
        while True:
            speak(tts, text)
            user_input = input("Press 'r' to reuse the same TTS model, or any other key to continue: ")
            if user_input.lower() != 'r':
                break
    

def speak(tts, text):
    print(f"Synthesizing text with {tts.model_name} ...")
    data = tts.tts(text)
    print("Audio synthesized!")
    sd.play(data, samplerate=22050)
    status = sd.wait()
    print(f"Audio played with status: {status}")


if __name__ == "__main__":
    main()