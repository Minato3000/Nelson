import pyttsx3 as pyt
import speech_recognition as sr
import datetime as dt
import os
import wikipedia
import webbrowser
import pywhatkit
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
import random
import time
from googletrans import Translator

r = sr.Recognizer()
mymic = sr.Microphone(device_index=1)
translator = Translator()

engine = pyt.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
engine.setProperty('rate', 180)
engine.setProperty('volume', 0.7)

def joke():
    joke1 = trans("bored of being bored because being bored is boring....ha ha ha ha ha ha")
    joke2 = trans("What do you call an Englishman with an IQ of 50?  Colonel, sir.....ha ha ha ha ha ha")
    joke3 = trans("They say an Englishman laughs three times at a joke. The first timewhen everybody gets it, the second a week later when he thinks he getsit, the third time a month later when somebody explains it to him.....ha ha ha ha ha ha")
    joke4 = trans("Why do cows wear bells?Because their horns don't work....ha ha ha ha ha ha")
    joke5 = trans("my life....ha ha ha ha ha ha")
    joke6 = trans("your life....ha ha ha ha ha ha")
    joke7 = trans("What did the buffalo say to his son when leaving for college ? bison....ha ha ha ha ha ha")
    joke8 = trans(" I visited my new friend in his flat. He told me to make myself at home. So I threw him out. I hate having visitors....ha ha ha ha ha ha")
    myjokes = [joke1, joke2, joke3, joke4, joke5, joke6, joke7, joke8]
    randomjoke = random.choice(myjokes)
    print(randomjoke)
    speak(randomjoke)

def motivation():
    moti1 = trans("its a shame for a man to grow old without seeing the beauty and strength his body is capable of")
    moti2 = trans("one whos ideal is mortal will die when his ideal dies , but when ones ideal is immortal he himself must become immortal to attain it")
    moti3 = trans("pain is only in the mind")
    moti4 = trans("Success is not how high you have climbed, but how you make a positive difference to the world.")
    moti5 = trans("Never lose hope. Storms make people stronger and never last forever.")
    moti6 = trans("strong men make great times,great times make weak men,weak men make tough times,tough times make strong men")
    moti7 = trans("All our dreams can come true, if we have the courage to pursue them.")
    moti8 = trans("The best time to plant a tree was 20 years ago. The second best time is now.")
    moti9 = trans("If people are doubting how far you can go, go so far that you can't hear them anymore.")
    moti10 = trans("Everything you can imagine is real.")
    moti = [moti1, moti2, moti3, moti4, moti5, moti6, moti7, moti8, moti9, moti10]
    randommoti = random.choice(moti)
    print(randommoti)
    speak(randommoti)

def list():
    how = trans("How are you - General interaction\nTell about yourself - About our virtual assistant\nwho are you - About our virtual assistant\nWhat can you do - Tell about the things VA can do \nTime - Will tell current date and time\nweather - Will tell weather of current location\njoke - Tell a joke\nmotivation - Tell a motivational quote\nopen <name> - Open the given website name\nsearch <name> - Search the given name in google\nIncrease volume - Will increase volume by 28% \nDecrease volume - Will decrease volume by 28%\nlaunch <app_name> - Launch apps in system \nopen uv - Element of surprise  \nSleep - Nelson will go to sleep")
    speak(how)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def trans(sentence):
    translated = translator.translate(sentence, dest='ta')
    return translated.text

def greet():
    hr = int(dt.datetime.now().hour)

    morning = trans("Good Morning")
    afternoon = trans("Good Afternoon")
    evening = trans("Good Evening")
    nelson = trans("I am Nelson!!, how can i help you?")

    if(hr>=0 and hr<12):
        speak(morning)
    elif(hr>=12 and hr<18):
        speak(afternoon)
    elif(hr>=18 and hr<20):
        speak(evening)
    speak(nelson)

def listen():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        listening = trans("Listening")
        speak(listening)
        print("Listening....")
        audio = rec.listen(source,phrase_time_limit=15)
    try:
        print("Recognizing...")
        query = rec.recognize_google(audio,language='en-in')
        query = query.lower()
        print("You said:", query ,"\n")
    except Exception as e:
        sayagaintxt = trans("say that again please")
        print("Say that again please")
        speak(sayagaintxt)
        return "None"
    return query

    #functions are defined 


def about():
    abouttxt1 = trans("I am Nelson....I was devloped by students of Artificial intelligence and data science department....")
    abouttxt2 = trans("I am still learning and open to criticism ")
    speak(abouttxt1)
    speak(abouttxt2)

def func():
    cantxt = trans("Things i can do")
    wanttxt = trans("What do you want to do?")
    speak(cantxt)
    speak("open applications , open websites , search things in google, play youtube videos , tell time and day , tell weather, tell jokes ,fun facts , motivational quotes , control system volume")
    speak(wanttxt)

def increse_vol():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    # Get current volume 
    currentVolumeDb = volume.GetMasterVolumeLevel()
    if currentVolumeDb > -5.409796714782715:
        volhightxt = trans("volume is more than 70 percent...please keep it below 70")
        print("volume is more than 70 percent...please keep it below 70")
        speak(volhightxt)
    else:
        volume.SetMasterVolumeLevel(currentVolumeDb  +6.0, None)
    # NOTE: -6.0 dB = half volume !

def set_vol(x):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    # Get current volume 
    currentVolumeDb = volume.GetMasterVolumeLevel()
    print(volume.GetMasterVolumeLevel())
    print(volume.GetVolumeRange())
    #volume.SetMasterVolumeLevel(currentVolumeDb  +6.0, None)
    # NOTE: -6.0 dB = half volume !


def decrese_vol():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    # Get current volume 
    currentVolumeDb = volume.GetMasterVolumeLevel()
    volume.SetMasterVolumeLevel(currentVolumeDb  -6.0, None)
    # NOTE: -6.0 dB = half volume !

  
#launch system apps
def app(query):
    appname = query[7:]
    print(appname)
    opentxt = trans("opening ")
    speak(opentxt + appname)
    appname = appname.replace(" ","")
    os.system(appname)

#open websites
def website(query):
    site = query[5:]
    opentxt = trans("opening website ")
    speak(opentxt+ site)
    site = site.replace(" ","")
    webbrowser.open("www."+site+".com")

#watch youtube videos
def youtube(query):
    utube = query[6:]
    opentxt = trans("Opening youtube ")
    openingtxt = trans(opentxt+utube)
    speak(openingtxt)
    pywhatkit.playonyt(utube)

def google_scearch(ques):
    query = ques
    for j in search(query,tld="co.in",num=10,stop=10,pause=2):
        return(j)

def gogo():
    sleepcomm = trans("Mention the duration you dont want me to disturb you")
    # comm = random.choice(slepcom)
    print(sleepcomm)
    speak(sleepcomm)

    ss = int(input("Enter the seconds to sleep: "))  #input is given manually we can convert it to be directly given by voice
    time.sleep(ss)

    backtxt = trans("nelson is back...yay")
    print("Nelson is back")
    speak(backtxt)
    

def weather():
    city = "chennai"
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    string = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    data = string.split('\n')
    time = data[0]
    sky = data[1]
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text
    pos = strd.find('Wind')
    other_data = strd[pos:]

    print("Temperature is", temp)
    print("Time: ", time)
    print('Sky Description:', sky)

    temptxt = trans("Temperature is "+ temp)
    skytxt = trans("The sky is"+ sky)
    speak(temptxt)
    speak(skytxt)

#main
if __name__ == "__main__":
    greet()
    while True:
        query=listen().lower()

        if "time" in query:
            now = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(now)
            speak(now)

        elif "joke" in query:
            joke()

        elif "motivation" in query:
            motivation()
        
        elif "tell about you" in query:
            about()

        elif "who are you" in query:
            about()

        elif "increase volume"  in query:
            increse_vol()
        
        elif "decrease volume" in query:
            decrese_vol()
 
        elif "what can you do" in query:
            func()

        elif "weather" in query:
            weather()

        elif "set" in query:
            y = query[10:]
            y  = float(y)
            k = y/100
            set_vol(k)
        
        #launch keyword to launch system apps
        elif "launch" in query:
            app(query)

        elif "open easwari" in query:
            webbrowser.open("https://ai.srmeaswari.ac.in/")    

        elif "open uv" in query:
            webbrowser.open("https://theuvofearth.wixsite.com/stage1")

        #open keyword to open websites
        elif "open" in query:
            website(query)

        #watch keyword to search and watch youtube videos
        elif "watch" in query:
            youtube(query)

        elif "search" in query: #returns the best website for asked query
            try:
                result = query[6:]
                givenbesttxt = trans("giving best results")
                speak(givenbesttxt)
                google_scearch(result)
                webbrowser.open(google_scearch(result))
            except:
                saysometxt = trans("please say something after search")
                print("please say something after search")
                speak(saysometxt)

        elif "how are you" in query:
            replytxt = trans("i am fine my boy...how about you ?")
            speak(replytxt)

        elif query=="show list":
            list()

        elif query=="sleep":
            gogo()

        elif query=="stop" or "end":
            exit()