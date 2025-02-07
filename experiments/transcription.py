# need open-ai whisper AND ffmpeg installed
# https://pypi.org/project/openai-whisper/

from env_utils import get_env_value
from openai import OpenAI

OPENAI_API_KEY = get_env_value('OPENAI_API_KEY')
print("API Key:", OPENAI_API_KEY)

client = OpenAI()

audio_file= open("/path/to/file/audio.mp3", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
)

print(transcription.text)