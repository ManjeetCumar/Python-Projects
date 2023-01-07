import pyttsx3 
import speech_recognition as sr
import pyjokes
import webbrowser, datetime

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing ...")
            data = recognizer.recognize_google(audio_data= audio)
            return data
        except sr.UnknownValueError:
            print("Unknown Value :(")
            return "I am Sorry! pardon"

def text_to_speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0])
    # rate = engine.getProperty('rate')
    engine.setProperty('rate', 100)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':
    while True:
        data = speech_to_text()
        if 'youtube' in data.lower():
            webbrowser.open("https://www.youtube.com/shorts/K5oyNw8r4mU")

        elif 'time' in data.lower():
            print(datetime.datetime.now())
            # text_to_speech(datetime.datetime.now())

        