'''
Refactor:
Change #defines to methods

See: http://stackoverflow.com/questions/4160175/detect-tap-with-pyaudio-from-live-mic
'''
#Libraries
import pyaudio
import struct
import math

#Variables
verbose = False
ITERATIONS = 100
MULTIPLICATIVE_CORRECTION = 10000
INITIAL_TAP_THRESHOLD = 0.015 * MULTIPLICATIVE_CORRECTION
FORMAT = pyaudio.paInt16
SHORT_NORMALIZE = (1.0/32768.0)
CHANNELS = 2
RATE = 44100
INPUT_BLOCK_TIME = 0.05
INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)
#If we get this many noisy blocks in a row, increase the threshold
OVERSENSITIVE = 15.0/INPUT_BLOCK_TIME
#If we get this many quiet blocks in a row, decrease the threshold
UNDERSENSITIVE = 120.0/INPUT_BLOCK_TIME
#If the noise was longer than this many blocks, it's not a 'tap'
MAX_TAP_BLOCKS = 0.15/INPUT_BLOCK_TIME

#Functions
def get_rms( block ):
    '''
    RMS amplitude is defined as the square root of the
    mean over time of the square of the amplitude.
    so we need to convert this string of bytes into
    a string of 16-bit samples.
    We will get one short out for each
    two chars in the string.
    '''
    count = len(block)/2
    format = "%dh"%(count) # https://mail.python.org/pipermail/tutor/2011-December/087531.html
    shorts = struct.unpack( format, block )

    #Iterate over the block.
    sum_squares = 0.0
    for sample in shorts:
        #Sample is a signed short in +/- 32768.
        #Normalize it to 1.0
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n
    return math.sqrt( sum_squares / count )

#Classes
class TapTester(object):
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.open_mic_stream()
        self.tap_threshold = INITIAL_TAP_THRESHOLD
        self.noisycount = MAX_TAP_BLOCKS+1
        self.quietcount = 0
        self.errorcount = 0

    def stop(self):
        self.stream.close()

    def find_input_device(self):
        if verbose == True:
            device_index = None
            for i in range( self.pa.get_device_count() ):
                devinfo = self.pa.get_device_info_by_index(i)
                print( "Device %d: %s"%(i,devinfo["name"]) )
                for keyword in ["mic","input"]:
                    if keyword in devinfo["name"].lower():
                        print( "Found an input: device %d - %s"%(i,devinfo["name"]) )
                        device_index = i
                        return device_index
            if device_index == None:
                print( "No preferred input found; using default input device." )
            return device_index
        else:
            device_index = None
            for i in range( self.pa.get_device_count() ):
                devinfo = self.pa.get_device_info_by_index(i)
                for keyword in ["mic","input"]:
                    if keyword in devinfo["name"].lower():
                        device_index = i
                        return device_index
            return device_index

    def open_mic_stream( self ):
        device_index = self.find_input_device()
        stream = self.pa.open(   format = FORMAT,
                                 channels = CHANNELS,
                                 rate = RATE,
                                 input = True,
                                 input_device_index = device_index,
                                 frames_per_buffer = INPUT_FRAMES_PER_BLOCK)
        return stream

    def adjust(self):
        finalThreshold = 0
        for i in range(0,ITERATIONS):
            try:
                block = self.stream.read(INPUT_FRAMES_PER_BLOCK)
            except IOError as e:
                self.errorcount += 1
                print( "(%d) Error recording: %s"%(self.errorcount,e) )
                self.noisycount = 1
                return
            amplitude = get_rms( block )
            if amplitude > self.tap_threshold:
                #Noisy block
                self.quietcount = 0
                self.noisycount += 1
                if self.noisycount > OVERSENSITIVE:
                    #Turn down the sensitivity
                    self.tap_threshold *= 1.1
            else:
                #Quiet block.
                if 1 <= self.noisycount <= MAX_TAP_BLOCKS:
                    self.tapDetected()
                self.noisycount = 0
                self.quietcount += 1
                if self.quietcount > UNDERSENSITIVE:
                    #Turn up the sensitivity
                    self.tap_threshold *= 0.9
            finalThreshold = finalThreshold + self.tap_threshold
        return finalThreshold
