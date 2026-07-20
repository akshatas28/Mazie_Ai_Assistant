# mega project 1
# jarvis

# in the right corner of vscode select interpretor
# click and create venv of py 3.12 
# then once successfully created run command : pip install speechrecognition pyaudio > both get successfully installed

# pip install setuptools
# pip install webbrowser
# pip install pyttsx3

# now new main.py

import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
ttsx= pyttsx3.init()

def speak(text):
  engine.say(text) # goes to queue
  engine.runAndWait() # processes the queue and waits until speaking is finished

# go to speech_recognition file online : github: microphone_recognition.py

if __name__=="__main__":
  speak("initializing mazie …")
  while True:
      # mega project 1
# jarvis

# in the right corner of vscode select interpretor
# click and create venv of py 3.12 
# then once successfully created run command : pip install speechrecognition pyaudio > both get successfully installed

# pip install setuptools
# pip install webbrowser
# pip install pyttsx3
# pip install pocketsphinx

# now new main.py

import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
ttsx= pyttsx3.init()

def speak(text):
  engine.say(text) # goes to queue
  engine.runAndWait() # processes the queue and waits until speaking is finished

# go to speech_recognition file online : github: microphone_recognition.py

if __name__=="__main__":
  speak("initializing mazie …")
  r = sr.Recognizer()
  
    try:
      with sr.Microphone() as source:
      print("say now")
      # listen for wake work: Max
      audio = r.listen(source, timeout=2, phrase_time_limit=1) # take input whatever is spoken
      # recognizes speech
     # here if only r.listen is mentioned and no timeout then input takes time so introduce timeout, also after per loop/cycle: the wait time can be reduced by introducing phrase_time_limit 
    
      #command = r.recognize_mazie(audio) : this funtion does not listen properly and the output is mostly inaccurate
      word = r.recognize_google(audio) # one can use multiple recognize_func where they can make use of ibm, whisper etc
      print(word)
      #print("Mazie thinks u said" + r.recognize_google(audio))
      if(command.lower()=="mazie"):
        speak("ya")
        # listening
        print("listening...")
        audio
      
      
    except Exception as e:
      print("Error{0}".format(e))
    #except sr.UnknownValueError:
      #print("Mazie thinks u said")
    #except sr.RequestError as e:
      #print("Mazie error {0}". format(e))
  

  
  
  
  

  
  
  # listen for wake work: Max
  audio = r.listen(source)