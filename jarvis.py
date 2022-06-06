import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing Jarvis")

MASTER = "Pratik"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

#will wish you according to time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour <12:
        speak ('Good Morning' +MASTER)

    elif hour>=12 and hour <18:
        speak ('Good Afternoon' +MASTER)

    else:
        speak ('Good Evening'+MASTER)
    
    speak("I am Jarvis. How may I help you")

#command from microphone   
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said:{query}\n")
    
    except Exception as e:
        print("Say that again please")
        query = None

    return query

def main():    
#speak("Initializing Jarvis")
    wishMe()
query = takeCommand()

#Logic for executing task as per query
if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query = query.replace('wikipedia', "")
    results = wikipedia.summary(query, sentences =2)
    print(results)
    speak(results)

elif 'open google' in query.lower():
    #webbrowser.open("google.com")

    url = 'https://www.google.com'

    chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(url)
   
elif 'open youtube' in query.lower():
    #webbrowser.open("youtube.com")

    url = "https://www.youtube.com"

    chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(url)

elif 'play music' in query.lower():
    songs_dir = "F:\Downloads\billboard1\billboard"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))
    