import speech_recognition as sr
import time
r=sr.Recognizer()
mic=sr.Microphone()
with mic as source:
    print('Say Something!')
    audio=r.listen(source)
r.recognize_google(audio)