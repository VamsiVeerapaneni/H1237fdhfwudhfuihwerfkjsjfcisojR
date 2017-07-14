# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 14:44:25 2017

@author: Krishna.Tiwari

"""
import speech_recognition as sr
import pyttsx
from gtts import gTTS
import os 
import time
from time import ctime
import sys

def recordData():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
    data = ""
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data
def con_data_text(data):
	engine=pyttsx.init()
	engine.say(data)
	engine.runAndWait()

def mellisa(data):
    if "who are you" in data:
        con_data_text('My name is mellisa')
   
    if "how are you" in data:
        con_data_text("I am fine thank you. What about you?")
 
    if "what time is it" in data:
        con_data_text(ctime()) 
    if "thank you" in data:
        con_data_text('thank you krishna, make a nice day')
        sys.exit("aa! errors!")

