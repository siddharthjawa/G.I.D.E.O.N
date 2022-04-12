from ast import Expression, Try
from email.mime import audio
from hashlib import new
import pyttsx3 
#pyttsx3 is a text-speech conversion
import speech_recognition as sr
#convert the spoken words into text
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio
'''dict1 = {"youtube", "google", "facebook", "reddit", "instagram", "web whatsapp", "the time", "prime video", "play music", "netflix", "spotify", "wikipedia", "open code", "send email"}'''
MASTER = 'Captain Tanisha'
print("Initializing GIDEON")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speak function will speak the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

# This function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning" +MASTER) 
        speak("What can I do for you?")
    elif hour>=12 and hour<18:
        speak("Good Afternoon" +MASTER)
        speak("What can I do for you?")
    else:
        speak("Good Evening" +MASTER)
        speak("What can I do for you?")

#This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        print("Please say that again")
        query = None

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('siddharthjawa@gmail.com', 'password')
    server.sendmail("parth.jawa@gmail.com", to, content)
    server.close()

#Main program starts now   
speak("Initializing Gideon...")
wishMe()
query = takeCommand()

#Logic for executing basic task as per the query
if 'wikipedia' in query.lower():
    speak('Searching Wikipedia')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences = 2)
    print(results)
    speak(results)
    
elif 'open youtube' in query.lower():
    webbrowser.open("youtube.com")
    '''url = 'youtube.com'
    brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\Brave.exe"
    webbrowser.get(brave_path).open(url)'''

elif 'open google' in query.lower():
    webbrowser.open("google.com")
    '''url = 'google.com'
    brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"
    webbrowser.get(brave_path).open(url)'''

elif 'open facebook' in query.lower():
    webbrowser.open("facebook.com")
    '''url = 'facebook.com'
    brave_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.exe %s"
    webbrowser.get(brave_path).open(url)'''

elif 'open reddit' in query.lower():
    webbrowser.open("reddit.com")
    '''url = 'reddit.com'
    brave_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.exe %s"
    webbrowser.get(brave_path).open(url)'''

elif 'open web whatsapp' in query.lower():
    webbrowser.open("web.whatsapp.com")
    '''url = 'web.whatsapp.com'
    brave_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.exe %s"
    webbrowser.get(brave_path).open(url)'''

elif 'open instagram' in query.lower():
    webbrowser.open("instagram.com")
    '''url = 'instagram.com'
    brave_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.exe %s"
    webbrowser.get(brave_path).open(url)'''

elif 'open netflix' in query.lower():
    webbrowser.open("netflix.com")
    '''url = 'netflix.com'
    brave_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.exe %s"
    webbrowser.get(brave_path).open(url)'''

elif 'open prime video' in query.lower():
    webbrowser.open("primevideo.com")
    '''url = 'primevieo.com'
    brave_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.exe %s"
    webbrowser.get(brave_path).open(url)'''

elif 'open spotify' in query.lower():
    webbrowser.open("spotify.com")
    '''url = 'spotify.com'
    brave_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.exe %s"
    webbrowser.get(brave_path).open(url)'''

elif 'play music' in query.lower():
    songs_dir = "C:\\Users\\siddh_9i3obh0\\Downloads\\Music"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))


elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} The time is {strTime}")

elif 'open code' in query.lower():
    codePath = "C:\\Users\\siddh_9i3obh0\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)

elif 'send email' in query.lower():
    try:
        speak("What should I send")
        content = takeCommand()
        to = "parth.jawa@gmail.com"
        sendEmail(to, content)
        speak("Email has been send successfully")

    except Exception as e:
        print(e)

