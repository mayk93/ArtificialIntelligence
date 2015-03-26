'''
Recording Client
'''
#Libraries
import speech_recognition as SpeechRecognition
import pyaudio

#Variables
DEFAULT_ENERGY_THRESHOLD = 15000
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

#Methods
def setup():
    recognizer = SpeechRecognition.Recognizer()
    recognizer.energy_threshold = DEFAULT_ENERGY_THRESHOLD
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
                    input=True, output=True,
                    frames_per_buffer=CHUNK_SIZE)
    return (recognizer,stream)
def listen(recognizerStreamTuple):
    recognizer,stream = recognizerStreamTuple
    with SpeechRecognition.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        stream.write(audio)
    except LookupError:
        print("Could not understand audio")
#Main
def main():
    listen(setup())

if __name__ == '__main__':
    main()
