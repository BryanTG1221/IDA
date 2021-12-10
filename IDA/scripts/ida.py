from math import trunc
import re
from PyQt5.QtCore import QThread
import requests
import pyttsx3
import speech_recognition as sr
import webbrowser 
import pywhatkit
import os
import pyautogui
import pyjokes
import envio
import DatosCorreo
import time
import win32console
import win32gui
from os import close, name
from subprocess import TimeoutExpired
from bs4.element import ResultSet
from bs4 import BeautifulSoup
from urllib.request import urlcleanup
from googletrans import Translator
from playsound import playsound

ventana= win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana,0)



#<---------------------------------------------Rutas--------------------------------------------->
def Sonidito():
    playsound('C:\\Program Files (x86)\\IDA\\rougue-studios\\IDA\\resources\\SonidoIDA.mp3')

def Spotify():
    os.startfile("C:\\Users\\Bryant\\AppData\\Roaming\\Spotify\\Spotify.exe")

def Chrome():
    os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
def Github():
    os.startfile("C:\\Users\\Bryant\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe")

def Whatsapp():
    os.startfile("C:\\Users\\Bryant\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

def SoniditoCloseIDA():
    playsound('C:\\Program Files (x86)\\IDA\\rougue-studios\\IDA\\resources\\CloseIDA.mp3')
#<-------------------------------------------Funciones------------------------------------------->

engine = pyttsx3.init()
voces = engine.getProperty('voices') 
engine.setProperty('voices',voces[2].id)
engine.setProperty('rate',170)

def habla(audio):
    print(" ")
    engine.say(audio)
    print(f": {audio}")
    engine.runAndWait()

def ejecutar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.2)        
        print("Escuchando...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        Sonidito()
        audio = r.listen(source,timeout=5)
        try:
            SoniditoCloseIDA()
            print("Entendiendo...")
            consulta = r.recognize_google(audio,language='es-mx')
            print(f"Dijiste: {consulta}")
        
        except Exception as Error:
            return "none"
        
        except TimeoutExpired as msg:
            print(msg)
                    
        except  sr.WaitTimeoutError as msg:
            print("El tiempo de espera ha terminado")
            quit()

        # Temporizador()
        return consulta.lower() 

def Respuestas():

    def AbrirApps():
        if 'spotify' in consulta:
            Spotify()
            habla("¡Hecho!")
        
        if 'modo uno' in consulta or 'modo programación' in consulta:
            habla('Modo programación activado')
            Spotify()
            Github()
            webbrowser.open("https://www.youtube.com")
            webbrowser.open("https://www.messenger.com")
            webbrowser.open("https://www.google.com")

        if 'whatsapp' in consulta:
            Whatsapp()
            habla('hecho')
        
    def Temperatura():
        buscar  = consulta
        url= f"https://www.google.com/search?q={buscar}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperatura = data.find("div", class_ = "BNeawe").text
        habla(f"La temperatura es de {temperatura} centígrados")

     
#<------------------------------------------Utilidades------------------------------------------->
    while True:
        consulta = ejecutar()   
        if 'abre spotify' in consulta:
            AbrirApps()
            
            break

        elif 'abre whatsapp' in consulta:
            AbrirApps()
            
            break

        elif 'temperatura' in consulta:
            Temperatura()
            
            break
        elif 'chiste' in consulta:
            chiste = pyjokes.get_joke(language='es', category= 'all')
            habla(chiste)
            
            break
#<------------------------------------------Saludos IDA------------------------------------------>
        elif 'hola' in consulta:
            habla("¡Hola!, como le puedo ayudar.")
        
        elif 'cómo estás' in consulta:
            habla("Lo siento, no fui programada para socializar.")
#<--------------------------------------------Breaks--------------------------------------------->
        elif 'necesitas un descanso' in consulta or 'tómate un descanso' in consulta:
            habla("Cerrando")
            break

        elif 'adiós' in consulta:
            habla("Cerrando")
            
            break

        elif 'no gracias' in consulta or 'gracias' in consulta:
            habla('Cerrando')
            break
#<-------------------------------------------Búsquedas------------------------------------------->
        elif 'en youtube' in consulta or 'un video' in consulta or 'el video' in consulta:
            habla("Esto es lo que encontré en youtube")
            consulta = consulta.replace('Busca a en youtube','')
            web = 'https://www.youtube.com/results?search_query=' + consulta
            webbrowser.open(web)
            habla("Listo")
            
            break
            
        elif 'en google' in consulta or 'qué es' in consulta or 'que pasaría si' in consulta or 'qué significa' in consulta or 'que necesito para' in consulta or 'cuándo' in consulta or 'quien' in consulta or 'cómo' in consulta or 'donde' in consulta or 'por qué' in consulta or 'definición' in consulta or 'porque' in consulta or 'cuál' in consulta or 'quién' in consulta or 'busca' in consulta:

            habla("Esto es lo que encontré:")
            consulta = consulta.replace("busca","")
            pywhatkit.search(consulta)
            
            break

        elif 'ayúdame con' in consulta or 'me podrías ayudar' in consulta or 'ayúdame' in consulta or 'ayudar' in consulta:
            habla('Claro, dime lo que necesites') 


        elif 'facebook' in consulta:
            habla('Abriendo facebook')
            webbrowser.open("https://www.facebook.com")
            habla("Listo")
            
            break

        elif 'messenger' in consulta:
            webbrowser.open("https://www.messenger.com/t/3004902926221849")
            habla("Hecho")
            
            break

        elif 'canción' in consulta or 'reproduce' in consulta:
            
            habla('Reproduciendo')
            cancion = consulta.replace('Reproduciendo','')
            pywhatkit.playonyt(cancion)
            habla("Listo")
            
            break
        elif 'abre youtube' in consulta:
            webbrowser.open("https://www.youtube.com")
            habla('Hecho')
            
            break

        elif 'abre chrome' in consulta:
            webbrowser.open("https://www.google.com")
            habla('Hecho')
            
            break
#<--------------------------------------------Correos-------------------------------------------->
        elif 'enviar correo' in consulta or 'envía un correo' in consulta or 'enviar un correo' in consulta or 'manda un correo' in consulta:
            envio.obtener_info_emails()  
            
            break
            
        elif 'agregar correo' in consulta or 'agrega un correo' in consulta or 'agregar un correo' in consulta  or 'agregar contacto' in consulta or 'agrega un contacto' in consulta or 'agregar un contacto' in consulta:
            DatosCorreo.obtener_datos()
            
            break
#<------------------------------------------Traducción------------------------------------------->
        elif 'traduce' in consulta or 'traducir' in consulta or 'traductor' in consulta:
            habla('Abriendo el traductor google')
            webbrowser.open("https://translate.google.com.mx/?hl=es")
            habla("Listo")
            
            break
#<--------------------------------------Descarga de videos--------------------------------------->
        elif 'descargar video' in consulta or 'descarga este video' in consulta or 'descargues un video' in consulta:
            habla('Abriendo página para descargar videos')
            webbrowser.open("https://www.y2mate.com/es55")
            habla("Listo")
            habla("Ingrese el enlace del video que quiera descargar")
            
            break

        elif 'cancela orden' in consulta or 'cancelar orden' in consulta:
            habla('Orden cancelada')

#<---------------------------------------------Modos--------------------------------------------->

        elif 'Modo uno' in consulta or 'modo programación' in consulta:
            AbrirApps()
            
            break

#<---------------------------------------------Extras--------------------------------------------->

        elif 'compra un jet' in consulta or 'cómprame un jet' in consulta:
            habla("Comprando jet")
            habla("Hacia donde quiere dirigirse")
            consulta = ejecutar()   
            habla("Dirigiéndose a " + consulta)
            break

        elif 'sube el volumen' in consulta:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            
            
        elif 'baja diez el volumen' in consulta or 'baja 10 el volumen' in consulta:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif 'sube diez el volumen' in consulta or 'sube 10 el volumen' in consulta:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            
            
        elif 'baja el volumen' in consulta:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")


        elif 'silencia el audio' in consulta or 'mutea el audio' in consulta:
            pyautogui.press("volumemute")
   
#<---------------------------------------------Final--------------------------------------------->
        # else:
        #     habla('Esta función no está disponible, ¿desea intentar de nuevo?')
            
Respuestas()
