import subprocess as sp
import numpy as np

FFMPEG_BIN = "c:\\temp\\ffmpeg\\bin\\ffmpeg.exe"
command = [ FFMPEG_BIN,
        '-i', 'c:\\temp\\test.mp3',
        '-f', 's16le',
        '-acodec', 'pcm_s16le',
        '-ar', '22050', # ouput will have 44100 Hz
        '-ac', '1', # stereo (set to '1' for mono)
        '-']
pipe = sp.Popen(command, stdout=sp.PIPE, bufsize=10**8)
raw_audio = pipe.proc.stdout.read(88200*4)
audio_array = np.fromarrays(raw_audio, dtype="int16")
np.savetxt("c:\\temp\\output.txt", audio_array)