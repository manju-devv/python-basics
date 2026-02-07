# pip3 install speechrecognition pyaudio
# pip3 install setuptools
# pip3 install pyttsx3

# import speech_recognition as sr
# import webbrowser
# import pyttsx3

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()


# def speak(text):
#     engine.say(text)
#     engine.runAndWait()


# if __name__ == "__main__":
#     speak("Initialising Jarvis!.....")
#     while True:
#         # listen for wake word jarvis
#         # obtain audio from microphone
#         r = sr.Recognizer()
#         print("recognizing.....")
#         try:
#             with sr.Microphone() as source:
#                 print("listening....")
#                 audio = r.listen(source, timeout=2, phrase_time_limit=1)
#             command = r.recognize_google(audio)
#             print(command)
#         except Exception as e:
#             print("something went wrong", e)


import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()

news_api = "01359dd4396d42dbb043815646365989"


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "open news" in c.lower():
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}"
        )
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles[:5]:
                speak(article["title"])
        else:
            print("Request failed:", r.status_code)
    else:
        speak("Cant process your request")


if __name__ == "__main__":
    speak("Initializing Jarvis")

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Mic calibrated")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)
            print("Recognizing...")
            word = recognizer.recognize_google(audio)
            print("You said:", word)
            if word.lower() == "hey jarvis":
                speak("Hey manju how can i help you!: ")
                with sr.Microphone() as source:
                    print("jarvis active.....")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Google API error:", e)
        except Exception as e:
            print("Error:", e)
