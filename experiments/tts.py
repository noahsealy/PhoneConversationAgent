# https://github.com/coqui-ai/TTS-papers
# coqui stopped being maintained, but a github fork under idiap is maintaining it
# https://github.com/idiap/coqui-ai-TTS
import torch
from TTS.api import TTS
import sounddevice as sd
import numpy as np
from torch.serialization import add_safe_globals
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig
from TTS.config.shared_configs import BaseDatasetConfig

# Add configs to safe globals (this addresses the security error)
add_safe_globals([XttsConfig, XttsAudioConfig, BaseDatasetConfig])

# Get device - check for MPS (Metal) first, then CUDA, then fall back to CPU
# device = "mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Get user input
text_to_speak = input("Enter the text you want to convert to speech: ")

# Run TTS with user input
wav = tts.tts(text=text_to_speak, speaker_wav="../audio_files/harvard.wav", language="en")
tts.tts_to_file(text=text_to_speak, speaker_wav="../audio_files/harvard.wav", language="en", file_path="output.wav")

# Optional: Play the audio directly (requires sounddevice library)

# Play the audio (wav is a numpy array)
sd.play(np.array(wav), samplerate=24000)
sd.wait()  # Wait until the audio is finished playing