import os
import speech_recognition as sr
import win32console
import win32gui
import sys
import pyttsx3
import icon
from playsound import playsound
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon,QMenu
from PyQt5.QtGui import QIcon
from playsound import playsound
ventana= win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana,0)

#<---------------------------------------------Rutas--------------------------------------------->
def Sonidito():
    playsound('C:\\Program Files (x86)\\IDA\\rougue-studios\\IDA\\resources\\SonidoIDA.mp3')
def IniciarIDA():
    os.startfile('C:\\Program Files (x86)\\IDA\\rougue-studios\\IDA\\scripts\\ida.py')
#<-------------------------------------------Funciones------------------------------------------->


engine = pyttsx3.init('sapi5')
voces = engine.getProperty('voices') 
engine.setProperty('voices',voces[2].id)
engine.setProperty('rate',150)

def habla(audio):
    print(" ")
    engine.say(audio)
    print(f": {audio}")
    engine.runAndWait()

def hacercomando():
    comando = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adaptándose al ruido de fondo.......")
        comando.adjust_for_ambient_noise(source,duration=0.5)
        print("Escuchando.......")
        comando.pause_threshold = 1
        comando.energy_threshold = 400
        audio = comando.listen(source)

        try:
            print("Entendiendo.......")
            consulta = comando.recognize_google(audio,language='es-mx')
            print(f"Dijiste: {consulta}")
            

        except Exception as Error:
            return "none"

        return consulta.lower() 
#<--------------------------------------------OYE IDA-------------------------------------------->
i=0
while True:
    if(i!=1):
        i+=1
        Sonidito()
        consulta = hacercomando()
        if 'oye' in consulta:
           IniciarIDA()
        elif 'estás ahí' in consulta or 'sigues ahí' in consulta or 'estás activada' in consulta:
            habla('Sí, aquí estoy')
        elif 'basta' in consulta:
            break
        else:
            print("Falsa alarma.......")
            
    consulta = hacercomando()
    if 'oye' in consulta:
        IniciarIDA()
    elif 'estás ahí' in consulta or 'sigues ahí' in consulta or 'estás activada':
        habla('Sí, aquí estoy')
    elif 'basta' in consulta:
        break
    else:
        print("Falsa alarma.......")






        







