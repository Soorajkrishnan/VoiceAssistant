import speech_recognition as sr
from tts import mouth
import os
import urllib2
import logging
os.system('jack_control start')

def is_connected():
    try:
        # Check Internt Connection
        urllib2.urlopen("https://www.google.com/")
        return True
    except urllib2.URLError, e:
        return False


conct = is_connected()
    # ----------------SPEECH-------------------------
recognizer = sr.Recognizer()
sr.Microphone.list_microphone_names()
mic = sr.Microphone(device_index=0)
os.system('clear')
    # -----------------------------------------------

def ear():
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    text=''
    if conct is True:
        # recognize speech using Google
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            mouth("Sorry, What did you said !")
            logging.info("Not Recognised")
            ear()
        except sr.RequestError as e:
            print("What's happening ? ; {0}".format(e))
            logging.error(e.message)
    else:
        # recognize speech using Sphinx
        try:
            text = recognizer.recognize_sphinx(audio)
            return text
        except sr.UnknownValueError:
            print("What did you said !")
        except sr.RequestError as e:
            print("What's happening ? ; {0}".format(e))
def hotword():
    try:
        hotw = recognizer.recognize_google(audio)
        return hotw
    except sr.UnknownValueError:
        print("What did you said !")
        mouth("Sorry..What did you said !")
    except sr.RequestError as e:
        print("What's happening ? ; {0}".format(e))
