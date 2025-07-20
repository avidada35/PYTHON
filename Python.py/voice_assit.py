import pyttsx3
import speech_recognition as sr
import datetime

def sptxt():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("listing...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print('recognizing...')
            data = recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print("failed to listen!")

sptxt()
