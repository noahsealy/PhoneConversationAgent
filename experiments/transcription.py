# need open-ai whisper AND ffmpeg installed
# https://pypi.org/project/openai-whisper/

import whisper

print(whisper.available_models())

model = whisper.load_model("tiny")
result = model.transcribe("../audio_input/harvard.wav")
print(result["text"])