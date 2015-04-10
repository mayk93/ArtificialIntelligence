from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave

THRESHOLD = 500
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 44100

def is_silent(snd_data):
    #"Returns 'True' if below the 'silent' threshold"
    return max(snd_data) < THRESHOLD

def normalize(snd_data):
    #"Average the volume out"
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r

def trim(snd_data):
    #"Trim the blank spots at the start and end"
    def _trim(snd_data):
        snd_started = False
        r = array('h')

        for i in snd_data:
            if not snd_started and abs(i)>THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    # Trim to the left
    snd_data = _trim(snd_data)

    # Trim to the right
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data

def add_silence(snd_data, seconds):
    #"Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
    r = array('h', [0 for i in range(int(seconds*RATE))])
    r.extend(snd_data)
    r.extend([0 for i in range(int(seconds*RATE))])
    return r

def record():
    """
    Record a word or words from the microphone and
    return the data as an array of signed shorts.

    Normalizes the audio, trims silence from the
    start and end, and pads with 0.5 seconds of
    blank sound to make sure VLC et al can play
    it without getting chopped off.
    """
    print("--->",0)
    p = pyaudio.PyAudio()
    print("--->",1)
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)
    print("--->",2)
    num_silent = 0
    snd_started = False

    r = array('h')
    print("--->","While:")
    while 1:
        print("--->","In while.")
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)
        print("--->","Wh-0")
        silent = is_silent(snd_data)

        if silent and snd_started:
            print("--->","Silent and sound started.")
            num_silent += 1
        elif not silent and not snd_started:
            print("--->","Not Silent and sound not started.")
            snd_started = True

        if snd_started and num_silent > 30:
            break

    print("--->",3)
    sample_width = p.get_sample_size(FORMAT)
    print("--->",4)
    stream.stop_stream()
    print("--->",5)
    stream.close()
    print("--->",6)
    p.terminate()
    print("--->",7)
    r = normalize(r)
    r = trim(r)
    r = add_silence(r, 0.5)
    return sample_width, r

def record_to_file(path):
    print("Recording started:")
    #"Records from the microphone and outputs the resulting data to 'path'"
    sample_width, data = record()
    #print("--->",0)
    data = pack('<' + ('h'*len(data)), *data)
    #print("--->",1)
    wf = wave.open(path, 'wb')
    #print("--->",2)
    wf.setnchannels(1)
    #print("--->",3)
    wf.setsampwidth(sample_width)
    #print("--->",4)
    wf.setframerate(RATE)
    #print("--->",5)
    wf.writeframes(data)
    #print("--->",6)
    wf.close()
    print("Recording ended:")

if __name__ == '__main__':
    print("Please speak a word into the microphone:")
    record_to_file('demo.wav')
    print("Done - result written to demo.wav .")
