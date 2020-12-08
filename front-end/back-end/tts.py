import pyttsx3
from pyttsx3 import voice
import os
import logging

def mouth(S):
    try:
        engine = pyttsx3.init();
        engine.setProperty('volume',0.9)
        engine.setProperty('voice', 'english')
        engine.say(S)
        print (S)
        engine.runAndWait()
    except Exception as e:
        logging.error(e.message)
