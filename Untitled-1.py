import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

assistantName = "Alice"
userName = "Arthur"


def Speak(audio):
    engine.say(audio)
    engine.runAndWait()



def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        Speak("Good Morning" + userName)

    elif hour>= 12 and hour<18:
        Speak("Good Afternoon" + userName)   

    else:
        Speak("Good Evening" + userName)  

    Speak("I am " + assistantName)



def Username():
    #uname = "takeCommand()"
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome", userName.center(columns))
    print("#####################".center(columns))
    Speak("how can I help?")

def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Unable to recognize your voice.")  
        return "None"

    return query






if __name__ == '__main__':
    clear = lambda: os.system('cls')
    # This Function will clean any
    # command before execution of this python file
    clear()
    WishMe()
    Username()
    listenFlag = False

    while True:
        wakeWord = takeCommand().lower()
        if 'hey' in wakeWord:
            Speak("yes?")
            listenFlag = True

        while listenFlag:
            query = takeCommand().lower()

            # All the commands said by user will be 
            # stored here in 'query' and will be
            # converted to lower case for easily 
            # recognition of command
            if 'wikipedia' in query:
                Speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 3)
                Speak("According to Wikipedia")
                print(results)
                Speak(results)

            elif 'open youtube' in query:
                Speak("okay mister brain rot\n")
                webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

            listenFlag = False