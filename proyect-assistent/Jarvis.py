from os import name
import pyttsx3
import speech_recognition as sr
import webbrowser 
import pywhatkit
import os
import wikipedia
import pyautogui

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
        print("Escuchando.......")
        comando.pause_threshold = 1
        audio = comando.listen(source)

        try:
            print("Entendiendo.......")
            consulta = comando.recognize_google(audio,language='es-mx')
            print(f"Dijiste: {consulta}")

        except Exception as Error:
            return "none"

        return consulta.lower() 

def Respuestas():

    def AbrirApps():
        habla("Ok, espera un segundo")
        if 'spotify' in consulta:
            os.startfile("C:\\Users\\Bryant\\AppData\\Roaming\\Spotify\\Spotify.exe")
        habla("Aplicación abierta con éxito")
        
    while True:
        consulta = hacercomando()

        if 'hola' in consulta:
            habla("Hola , soy Rebe")
            habla("Su asistente personal")
            habla("¿Cómo le puedo ayudar?")

        elif 'báñate' in consulta:
            habla("ya voy señor")
            break

        elif 'un chiste' in consulta:
            habla("Había una vez un pollito que se llamaba pegamento, se cayó y se pegó JA JA JA JA JA")

        elif 'necesitas un descanso' in consulta or 'tómate un descanso' in consulta:
            habla("Ok señor, pero puede hablarme cuando lo necesite")
            break

        elif 'hueles feo' in consulta:
            habla("Lo siento señor, ya me tomaré un baño")  

        elif 'adiós' in consulta:
            habla("Adiós")
            break

        elif 'gracias' in consulta:
            habla("De nada, nos vemos pronto")
            break

        elif 'huele a caca' in consulta:
            habla("Mejor que se bañe que hasta acá huele a pedo")

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
Respuestas()

