#Libraries
import adjuster
import speech_recognition as SpeechRecognition

#Functions
'''
This method adjusts the sensitivity based on
type of microphone input.
'''
def getThreshold():
    thresholdAdjuster = adjuster.TapTester()
    return thresholdAdjuster.adjust()

def initialize():
    Recognizer = SpeechRecognition.Recognizer()
    Recognizer.energy_threshold = getThreshold()
    print(Recognizer.energy_threshold)
    return Recognizer

def listen(Recognizer):
    with SpeechRecognition.Microphone() as source:
        audio = Recognizer.listen(source)
    try:
        print("You said:",Recognizer.recognize(audio))
    except LookupError:
        print("Could not understand audio")

def main():
    listen(initialize())

if __name__ == '__main__':
    main()
