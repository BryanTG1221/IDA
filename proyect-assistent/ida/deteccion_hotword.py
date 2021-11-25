from playsound import playsound
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
from playsound import playsound
import icon
#pip install PyQt5  
ventana= win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana,0)

#<-----------------------------------------Base de datos----------------------------------------->
cred = credentials.Certificate('C:\\Program Files (x86)\\IDA\\rougue-studios\\proyect-assistent\\ida\\assistent-personal-35dbb-firebase-adminsdk-1sx5y-058487df7f.json')
firebase_admin.initialize_app(cred,{'databaseURL':'https://assistent-personal-35dbb-default-rtdb.firebaseio.com/'})
#<-------------------------------------------Funciones------------------------------------------->
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
        playsound('C:\\Program Files (x86)\\IDA\\rougue-studios\\resources\\SonidoIDA.mp3')
        consulta = hacercomando()
        if 'oye' in consulta:
            os.startfile('C:\\Program Files (x86)\\IDA\\rougue-studios\\proyect-assistent\\ida\\ida.py')
            ref=db.reference('/calls/IDA/oye')
            resultado=ref.get()
            resultado=resultado+1
            ref=db.reference('/calls/IDA')
            ref.update({'oye':resultado})
        elif 'basta' in consulta:
            break
        else:
            print("Falsa alarma.......")
    else:
        consulta = hacercomando()
        if 'oye' in consulta:
            os.startfile('C:\\Program Files (x86)\\IDA\\rougue-studios\\proyect-assistent\\ida\\ida.py')
            ref=db.reference('/calls/IDA/oye')
            resultado=ref.get()
            resultado=resultado+1
            ref=db.reference('/calls/IDA')
            ref.update({'oye':resultado})
        elif 'basta' in consulta:
            break
        else:
            print("Falsa alarma.......")



    


        







