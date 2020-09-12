import time
import webbrowser
from datetime import datetime
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import random
import os

r = sr.Recognizer()


def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = " "
        try:
            voice = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('I do not understand')
        except sr.RequestError:
            speak("System is not working.")
        return voice


def response(voice):
    if "hi" in voice:
        print("Hi Mahmut.What can I do for you?")
        speak("hi mahmut.what can I do for you?")

    if 'what time' in voice:
        print(datetime.now().strftime('%H:%M:%S'))
        speak(datetime.now().strftime('%H:%M:%S'))

    if 'my information' in voice:
        print("Ok! I am reading")
        speak("Ok! I am reading")
        with open('my_information.txt') as file:
            file = file.read()

        seslendir = gTTS(file)
        seslendir.save("text_to_speech.wav")
        os.system("text_to_speech.wav")

    if 'open programs' in voice:
        print("I show applications")
        speak("I show applications")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs')

    if 'search the internet' in voice:
        print("what do you want me to search on google")
        search = record('what do you want me to search on google')
        url = 'https://www.google.com.tr/search?q=' + search
        webbrowser.get().open(url)
        print(search+" Search results for")
        speak('I found these on Google ' + search)

    if 'play video' in voice:
        print('What do you want me to play on youtube')
        search = record('what do you want me to play on youtube')
        url = 'https://www.youtube.com/results?search_query=' + search
        webbrowser.get().open(url)
        print('Ok i search for you ' + search)
        speak('I found these on YouTube ' + search)

    if 'weather forecast' in voice:
        url = 'https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=%C4%B0stanbul'
        webbrowser.get().open(url)
        print('Ok! I show the weather')
        speak('Ok! I show the weather')

    if 'show my notes' in voice:
        speak("Ok!")
        url = 'https://obs.beykent.edu.tr/oibs/ogrenci/login.aspx'
        webbrowser.get().open(url)
        print('You must login to find out your grades ')
        speak('You must login to find out your grades ')

    if 'send email' in voice:
        print("Ok! I am sending")
        speak("Ok! I am sending")
        url = 'https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
        webbrowser.get().open(url)
        print('You must log in to send mail')
        speak('You must log in to send mail')

    if 'bye-bye' in voice:
        print("See you")
        speak("see you")
        exit()


def speak(string):
    tts = gTTS(string)
    rand = random.randint(1, 10000)
    file = 'audio.' + str(rand) + '.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)


print ("How can i help you?")
speak("How can i help you")
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)
