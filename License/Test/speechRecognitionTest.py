try:
    print("Importing")
    import speech_recognition as sr
    print("Imported")
except Exception as e:
    print("Exception: ",e)

r = sr.Recognizer()
r.energy_threshold = 15000

with sr.Microphone() as source:
    audio = r.listen(source)

try:
    print("You said " + r.recognize(audio))
except LookupError:
    print("Could not understand audio")
