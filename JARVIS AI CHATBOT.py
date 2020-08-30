import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import pyaudio
import os
import smtplib
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak('good morning')
    elif hour>=12 and hour<15:
        speak('good afternoon')
    elif hour>=15 and hour<21:
        speak('good evening')
    else:
        speak(' good night')

    speak('i am Raahul, please tell me how may i help you sir')
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit=8)
    try:
        print('recognising...')
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        #print(e)
        print('say that again please')
        return 'none'
    return query
ques = ['what is your name','where are you from','do you want to be my friend']
ans = ['i am rahul sir','i am from bihar','yes sir ofcourse']
if __name__ == '__main__':
    #speak('rohit is a good boy')
    wishme()
    while True:
    #if 1:
     query = takecommand().lower()
     #if 'how are you' in query:
         #speak('i am good,how are you')

     if 'wikipedia' in query:
         speak('searching wikipedia..')
         query = query.replace('wikipedia',"")
         result = wikipedia.summary(query,sentences=2)
         speak('according to wikipedia')
         speak(result)
     elif 'open youtube' in query:
         webbrowser.open('youtube.com')
     #elif 'who are you' in query:
         #speak('i am Raahul a underworld don')

     #elif 'where are you from' in query:
         #speak('i am from bihar, thook ke mathaa me ched kar denge')
     #elif 'you want to be my friend' in query:
         #speak('no, maii kisi ka doost nahi banta')
     for q,a in zip(ques,ans):
         if q in query:
             speak(a)



     #else:
         #quit()








