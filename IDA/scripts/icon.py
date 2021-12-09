from PyQt5.QtWidgets import QApplication, QSystemTrayIcon,QMenu
from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon,QMenu
from PyQt5.QtGui import QIcon
from firebase_admin import credentials
from firebase_admin import db
import os
import speech_recognition as sr
import win32console
import win32gui
import sys
import firebase_admin
import playsound as playsound
import pyttsx3

# ventana= win32console.GetConsoleWindow()
# win32gui.ShowWindow(ventana,0)

#<---------------------------------------------Rutas--------------------------------------------->
def Sonidito():
    playsound('C:\\Program Files (x86)\\IDA\\rougue-studios\\IDA\\resources\\SonidoIDA.mp3')
def IniciarIDA():
    os.startfile('C:\\Program Files (x86)\\IDA\\rougue-studios\\IDA\\scripts\\ida.py')
def IniciarIDAAutomatico():
    os.startfile('C:\\Program Files (x86)\\IDA\\rougue-studios\\IDA\\scripts\\ida_automatico.py')

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
        
        comando.adjust_for_ambient_noise(source,duration=0.5)
        print("Escuchando...")
        comando.pause_threshold = 1
        comando.energy_threshold = 400
        audio = comando.listen(source)

        try:
            print("Entendiendo...")
            consulta = comando.recognize_google(audio,language='es-mx')
            print(f"Dijiste: {consulta}")
            

        except Exception as Error:
            return "none"

        return consulta.lower() 
#<--------------------------------------------OYE IDA-------------------------------------------->

#<-------------------------------------------Funciones------------------------------------------->

app=QApplication(sys.argv)
TrayIcon= QSystemTrayIcon(QIcon('C:\\Program Files (x86)\\IDA\\rougue-studios\\IDA\\resources\\iconoTask1000.png'),parent=app)
TrayIcon.setToolTip('IDA')
TrayIcon.show()

menu=QMenu()
exitAction=menu.addAction('Salir')
exitAction.triggered.connect(app.quit)
TrayIcon.setContextMenu(menu)



i=0
while True:
    if(i!=1):
        i+=1       
        consulta = hacercomando()
        if 'oye' in consulta or 'modo simple' in consulta:
            IniciarIDA()
        elif 'modo automático' in consulta:
            IniciarIDAAutomatico()
        elif 'basta' in consulta:
            habla('Saliendo')
            break
        else:
            print("Falsa alarma...")
            
    consulta = hacercomando()
    if 'oye' in consulta or 'modo simple' in consulta:
        IniciarIDA()
    elif 'modo automático' in consulta:
        IniciarIDAAutomatico()
    elif 'estás ahí' in consulta or 'sigues ahí' in consulta or 'estás activada' in consulta:
        habla('Sí, aquí estoy')
    elif 'basta' in consulta:
        habla('Saliendo')
        break
    else:
        print("Falsa alarma...")

sys.exit()



