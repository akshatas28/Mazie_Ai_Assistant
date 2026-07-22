# mega project 1
# mazie

# in the right corner of vscode select interpretor
# click and create venv of py 3.12 
# then once successfully created run command : pip install speechrecognition pyaudio > both get successfully installed

# now new main.py
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

def speak(text):
  engine.say(text) # goes to queue
  engine.runAndWait() # processes the queue and waits until speaking is finished

# go to speech_recognition file online : github: microphone_recognition.py

if __name__=="__main__":
  speak("initializing mazie …")
  while True:
      # mega project 1
# mazie

# in the right corner of vscode select interpretor
# click and create venv of py 3.12 
# then once successfully created run command : pip install speechrecognition pyaudio > both get successfully installed

# pip install setuptools
# pip install webbrowser
# pip install pyttsx3
# pip install pocketsphinx
# pip install gTTS
# pip install groq
# pip install pygame
# use elevenlabs for professional voice
# safe function for apple ios
# now new main.py
import requests
from gtts import gTTS
from groq import groq
import pygame
import os

# Go to newsapi and login, key will be generated
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "your-api-key"

def speak_old(text):
  engine.say(text) # goes to queue
  engine.runAndWait() # processes the queue and waits until speaking is finished

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init() # initialize file
    pygame.mixer.music.load('temp.mp3') # load mp3 file
    pygame.mixer.music.play() # play mp3 file
    while pygame.mixer.music.get_busy(): # keep music running until code stops
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove('temp.mp3')

# go to speech_recognition file online : github: microphone_recognition.py

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1] # here: if we provide input : play skyfall : it gets converted to ["play", "skyfall"] and as skyfall is at 1 number so that will be considered
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data=r.json()
            articles=data.get('articles', []) # extracting headlines
            for article in articles:
                speak(article['title'])
    else:
        # let ai handle the request
        output=aiprocess(c)
        speak(output)
        

# client.py
# Go to Groq api key and generate api key
def aiprocess():
  client = groq(api_key="self_key")
  completion = client.chat.completion.create(model="current_groq_model", message=[{"role": "system" , "content" : "you are a virtual assitant named mazie, skilled in general tasks like alexa and siri, give short responses" }, {"role": "user" , "content" : command } ])  
  return completion.choices[0].message.content


if __name__=="__main__":
  speak("initializing mazie …")
  
  while true:
    r = sr.Recognizer()
    try:
      with sr.Microphone() as source:
          print("say now")
      # listen for wake work: Max
          audio = r.listen(source, timeout=2, phrase_time_limit=1) # take input whatever is spoken
      # recognizes speech
     # here if only r.listen is mentioned and no timeout then input takes time so introduce timeout, also after per loop/cycle: the wait time can be reduced by introducing phrase_time_limit 
      #recognize_mazie(audio) : this funtion does not listen properly and the output is mostly inaccurate
      word = r.recognize_google(audio) # one can use multiple recognize_func where they can make use of ibm, whisper etc
      print(word)
      #print("Mazie thinks u said" + r.recognize_google(audio))
      if(word.lower()=="mazie"):
        speak("ya")
        # listening
        with sr.Microphone() as source:
          print("say the command")
      # listen for command
          audio = r.listen(source, timeout=2, phrase_time_limit=1)
          command = r.recognize_google(audio)
          processCommand(command)
        print("listening...")
    except Exception as e:
      print("Error{0}".format(e))
    #except sr.UnknownValueError:
      #print("Mazie thinks u said")
    #except sr.RequestError as e:
      #print("Mazie error {0}". format(e))
  

  
# in musicLibrary.py file

music = {"stealth":"https://www.youtube.com/watch?v=U47Tr9BB_wE", "march" : "https://www.youtube.com/watch?v=Xqeq4b5u_Xw", "skyfall" : "https://www.youtube.com/watch?v=DeumyOzKqgI&pp=ygUHc2t5ZmFsbA%3D%3D" , "wolf" : "https://youtu.be/gSZKqzlTDJ0?si=10M_DzyKlmM7ys95" }