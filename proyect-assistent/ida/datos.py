from math import inf
from email.message import EmailMessage
from subprocess import TimeoutExpired
from firebase_admin import credentials
from firebase_admin import db
from playsound import playsound
import smtplib
import speech_recognition as sr
import pyttsx3
import re
import firebase_admin

#<-------------------------------------------Funciones------------------------------------------->
listener = sr.Recognizer()
Asistente = pyttsx3.init()

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
        playsound('C:\\Program Files (x86)\\IDA\\rougue-studios\\resources\\SonidoIDA.mp3')
        audio = comando.listen(source,timeout=5)

        try:
            print("Entendiendo.......")
            consulta = comando.recognize_google(audio,language='es-mx')
            print(f"Dijiste: {consulta}")

        except Exception as Error:
            return "none"
        
        except TimeoutExpired as msg:
            print(msg)
        
        except sr.WaitTimeoutError as msg:
            print("El tiempo de espera ha terminado")
            quit()

        return consulta.lower()
    
def enviar_datos():
        print('Hola')

def obtener_datos():
    habla('nombre del contacto')
    nombre = hacercomando()
    habla('cual es la terminacion del correo?')
    habla('Gmail,Hotmail,Outlook')
    terminacioncorreo= hacercomando()
    if 'gmail' in terminacioncorreo or 'hotmail' in terminacioncorreo or 'outlook' in terminacioncorreo:
        habla('Okay')
        habla('diga el correo antes del arroba')
        correo=hacercomando()
        correo = correo.replace(' ','')
        correofull = correo + '@' + terminacioncorreo + '.com'
        print(correofull)
        subir_info(nombre,correofull)
    habla('No es una direccion valida')
    habla('Opciones validas: Gmail , Outlook, Hotmail')
    terminacioncorreo=hacercomando()
    if 'gmail' in terminacioncorreo or 'hotmail' in terminacioncorreo or 'outlook' in terminacioncorreo:
        habla('Okay')
        habla('diga el correo antes del arroba')
        correo=hacercomando()
        correo = correo.replace(' ','')
        correofull = correo + '@' + terminacioncorreo + '.com'
        print(correofull)
        subir_info(nombre,correofull)
    habla('No es un correo valido, vuelva a intentarlo')

def subir_info(nombre,correo):
    ref = db.reference('/Correos')
    datos = {'nombre':nombre,'correo':correo}
    ref.child(nombre).set(datos)
    habla('el correo se agrego con exito')
    ref=db.reference('/calls/Emails/Agregados')
    resultado = ref.get()
    resultado=resultado+1
    ref=db.reference('/calls/Emails')
    ref.update({'Agregados':resultado})
    print(resultado)

def obtener_correo(nombre):
    ref =db.reference('/Correos/'+nombre+'/correo')
    resultado = ref.get()
    #resultado= ref.order_by_child("nombre").equal_to(nombre).get()
    print(resultado)
    return(resultado)

def altasfirebase():
    ref = db.reference('/calls')
    datos={'Agregados':0,'Enviados':0}
    ref.child('Emails').set(datos)


    



