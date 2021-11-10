from os import name
import requests
from bs4 import BeautifulSoup
from urllib.request import urlcleanup
from googletrans import Translator
import pyttsx3
import speech_recognition as sr
import webbrowser 
import pywhatkit
import os
import wikipedia
import pyautogui
import envio
import datos
#

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('C:\\Users\\bryan\Documents\\IDA\\rougue-studios\\proyect-assistent\\ida\\assistent-personal-35dbb-firebase-adminsdk-1sx5y-058487df7f.json')
firebase_admin.initialize_app(cred,{'databaseURL':'https://assistent-personal-35dbb-default-rtdb.firebaseio.com/'})



Asistente = pyttsx3.init('sapi5')
voces = Asistente.getProperty('voices') #voices es el nombre de la propiedad, no se puede modificar 
Asistente.setProperty('voices',voces[0].id)
Asistente.setProperty('rate',180)

def habla(audio):
    print(" ")
    Asistente.say(audio)
    print(f": {audio}")
    Asistente.runAndWait()

def hacercomando():
    comando = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adaptándose al ruido de fondo.......")
        comando.adjust_for_ambient_noise(source,duration=0.2)
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

def Respuestas():

    def Traducir():
        habla("¿A que idioma quieres traducir?")
        consulta = hacercomando()
        if  'español' in consulta:
            traslate = Translator()
            habla("Dime lo que quieras traducir")
            line = hacercomando()
            result = traslate.translate(line,src= "auto", dest="es")
            Text = result.text
            habla(Text)
            
        elif  'inglés' in consulta:
            traslate = Translator()
            habla("Dime lo que quieras traducir")
            line = hacercomando()
            result = traslate.translate(line,src= "auto", dest="en")
            Text = result.text
            habla(Text)

        elif 'chino' in consulta:
            traslate = Translator()
            habla("Dime lo que quieras traducir")
            line = hacercomando()
            result = traslate.translate(line,src= "auto", dest="zh-cn")
            Text = result.text
            habla(Text)

        elif 'ruso' in consulta:
            traslate = Translator()
            habla("Dime lo que quieras traducir")
            line = hacercomando()
            result = traslate.translate(line,src= "auto", dest="russian")
            Text = result.text
            habla(Text)
            
    def AbrirApps():
        habla("Ok, espera un segundo")
        if 'spotify' in consulta:
            os.startfile("C:\\Users\\Bryant\\AppData\\Roaming\\Spotify\\Spotify.exe")
        habla("Aplicación abierta con éxito")
        if 'teams' in consulta:
            os.startfile("C:\\Users\\Bryant\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart 'Teams.exe'")
        habla("Aplicación abierta con éxito")
        
    def Temperatura():
        buscar  = "Temperatura en Nuevo Laredo"
        url= f"https://www.google.com/search?q={buscar}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperatura = data.find("div", class_ = "BNeawe").text
        habla(f"La temperatura es de {temperatura} centígrados")
    while True:
        consulta = hacercomando()   

        if 'hola' in consulta:
            habla("Hola , soy Aída")
            habla("Su asistente personal")
            habla("¿Cómo le puedo ayudar?")

        elif 'un chiste' in consulta:
            habla("Había una vez un pollito que se llamaba pegamento, se cayó y se pegó JA JA JA JA JA")

        elif 'necesitas un descanso' in consulta or 'tómate un descanso' in consulta:
            habla("Ok señor, pero puede hablarme cuando lo necesite")
            break

        elif 'adiós' in consulta:
            habla("Adiós")
            break

        elif 'gracias' in consulta:
            habla("De nada, nos vemos pronto")
            break

        elif 'en youtube' in consulta or 'un video' in consulta or 'el video' in consulta:
            habla("Esto es lo que encontré en youtube")
            consulta = consulta.replace('Busca a en youtube','')
            web = 'https://www.youtube.com/results?search_query=' + consulta
            webbrowser.open(web)
            habla("Listo")
            
        elif 'en google' in consulta:
            habla("Esto es lo que encontré en google!")
            consulta = consulta.replace("busca en google","")
            pywhatkit.search(consulta)
            habla("Listo")

        elif 'facebook' in consulta:
            habla('Abriendo facebook')
            webbrowser.open("https://www.facebook.com")
            habla("Listo")

        elif 'canción' in consulta or 'reproduce' in consulta:
            
            habla('Reproduciendo')
            cancion = consulta.replace('Reproduciendo','')
            pywhatkit.playonyt(cancion)
            habla("Listo")

        elif 'abre spotify' in consulta:
            AbrirApps()

        elif 'temperatura' in consulta:
            Temperatura()

        elif 'enviar correo' in consulta:
            envio.obtener_info_emails()  
            
        elif 'agregar correo' in consulta:
            datos.obtener_datos()
            
        elif 'traduce' in consulta or 'traducir' in consulta or 'traductor' in consulta:
            habla('Desea traducir algo corto o algo largo')
            consulta=hacercomando()
            if 'corto' in consulta:
                Traducir()
            elif 'largo' in consulta:
                habla('Abriendo el traductor google')
                webbrowser.open("https://translate.google.com.mx/?hl=es")
                habla("Listo")

        elif 'descargar video' in consulta or 'descarga este video' in consulta or 'descargues un video' in consulta:
            habla('Abriendo página para descargar videos')
            webbrowser.open("https://www.y2mate.com/es55")
            habla("Listo")
            habla("Ingrese el enlace del video que quiera descargar")

        

        
Respuestas()
