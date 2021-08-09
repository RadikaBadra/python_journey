#import pyttxs3
import pyttsx3
#import subprocess
import subprocess
#import speech recognition
import speech_recognition as sr
#import wikipedia
import wikipedia
import time
import sys
#buat variabel
r = sr.Recognizer()
voice = pyttsx3.init()
voice.say("i'm your assistant, what i can do for you")
voice.runAndWait()

def micread():
    with sr.Microphone() as source :
        print("talk")
        audio_text = r.listen(source)
        text = ''
        split_text = ''
        print("Recognizing")

        try :
            text = r.recognize_google(audio_text)
            print('you said : ' + text)
            split_text = text.split()
        except:
            print("please said something")
            voice.say("please said something")
            voice.runAndWait()
        return split_text

def command(audiotext):
    
    text = ' '.join(audiotext)
    split_text = audiotext
    if 'how' and 'are' and 'you' in audiotext:
        print("fine")
        voice.say("fine")
        voice.runAndWait()
        
    elif 'music' in audiotext or 'spotify' in audiotext :
        print(text)
        voice.say(text)
        voice.runAndWait()
        subprocess.call('C://Users//ASUS//AppData//Roaming//Spotify//Spotify.exe')
    
    elif 'search' in audiotext or 'wikipedia' in audiotext:
        
        if split_text == 2:
            result = wikipedia.search(split_text[1] ,results = 1, suggestion=False)
        else :
            result = wikipedia.search(text ,results = 1, suggestion=False)

        for search in result :
            print(search)
            print(wikipedia.summary(search, sentences=2))
            voice.say(wikipedia.summary(search, sentences=2))
            voice.runAndWait()
    
    elif 'set' and 'timer' in audiotext :
        voice.say('how many second the timer is')
        voice.runAndWait()
        t = abs(int(input('how many second : ')))
        
        for t in range(t,0,-1):
            m , s = divmod(t, 60)
            h , m = divmod(m, 60)
            timer = '{:02d}:{:02d}:{:02d}'. format(h,m,s)
            print(timer + "\r", end="\r")
            time.sleep(1)
            t -= 1
        print("time is up")
        voice.say("time is up")
        voice.runAndWait()
            
    elif 'turn' and 'off' in audiotext :
        voice.say("turning off")
        voice.runAndWait()
        print('turning off...')
        time.sleep(1)
        sys.exit()
        
while True:
    mic = micread()
    for i in range(len(mic)):
        mic[i] = mic[i].lower()
    audiotext = mic
    command(audiotext)
    
   