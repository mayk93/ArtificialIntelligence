#import pyaudio

#!/usr/bin/env python
from ctypes import *
import pyaudio
import socket
import sys
import time
import os

# From alsa-lib Git 3fd4ab9be0db7c7430ebd258f2717a976381715d
# $ grep -rn snd_lib_error_handler_t
# include/error.h:59:typedef void (*snd_lib_error_handler_t)(const char *file, int line, const char *function, int err, const char *fmt, ...) /* __attribute__ ((format (printf, 5, 6))) */;
# Define our error handler type
ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
def py_error_handler(filename, line, function, err, fmt):
  print('')
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

asound = cdll.LoadLibrary('libasound.so.2')
# Set error handler
asound.snd_lib_error_set_handler(c_error_handler)
# Initialize PyAudio
p = pyaudio.PyAudio()
p.terminate()

print('-'*40)
# Reset to default error handler
asound.snd_lib_error_set_handler(None)
# Re-initialize
p = pyaudio.PyAudio()
p.terminate()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Created socket')
except socket.error:
    print('Failed to create socket')
    sys.exit()
 
host = '104.155.13.116';
port = 5555;

import speech_recognition as sr
r = sr.Recognizer()
r.energy_threshold = 150
print("Listening:")
with sr.Microphone() as source:                # use the default microphone as the audio source
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
    s.sendto(audio, (host, port))
'''
try:
    print("You said: " + r.recognize(audio))    # recognize speech using Google Speech Recognition
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
'''
d = s.recvfrom(1024)
reply = d[0]
addr = d[1]
print('Server reply : ' + reply.decode('utf-8'))
