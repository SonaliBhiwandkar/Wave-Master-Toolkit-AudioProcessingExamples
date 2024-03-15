#wave_example.py
# Audio file formats
# .mp3
# .flac
# .wav

import wave

# Audio signal parameters
# - number of channels
# - sample width
# - framerate/sample_rate: 44,100 Hz
# - number of frames
# - values of a frame

obj = wave.open("audio1.wav", "rb")   #read it in binary

print("Number of channels", obj.getnchannels())
print("Sample Width", obj.getsampwidth())
print("Frame rate", obj.getframerate())
print("Number of Frames", obj.getnframes())
print("parameters", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

frames = obj.readframes(-1) #read all frames
print(type(frames), type(frames[0]))
print(len(frames) / 2)

obj.close()

obj_new = wave.open("audio1new.wav", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(48000.0)

obj_new.writeframes(frames)

obj_new.close()