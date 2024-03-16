#load_mp3.py
import os
from pydub import AudioSegment

# Add the directory containing FFmpeg executable to PATH
ffmpeg_directory = r"#path to bin of ffmpeg"
os.environ["PATH"] += os.pathsep + ffmpeg_directory

audio = AudioSegment.from_wav("audio1.wav")

# Increase the volume by 6db
audio = audio + 6

audio = audio * 2

audio = audio.fade_in(2000)

audio.export("mashup.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("mashup.mp3")
print("done")
