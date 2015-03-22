#Libraries
import adjuster
import speech_recognition as SpeechRecognition

#Auxiliary Functions
'''
This method adjusts the sensitivity based on
type of microphone input.
'''
def getThreshold():
    #5000 and 15000
    tester = adjuster.TapTester()
    threshold = tester.listen()
    print(threshold)
    return threshold

#Variables
Recognizer = SpeechRecognition.Recognizer()
Recognizer.energy_threshold = getThreshold()

#Functions
with SpeechRecognition.Microphone() as source:
    audio = Recognizer.listen(source)

try:
    print("You said:",Recognizer.recognize(audio))
except LookupError:
    print("Could not understand audio")
