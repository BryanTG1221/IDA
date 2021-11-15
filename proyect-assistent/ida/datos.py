from math import inf
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
import re
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pyrebase
from playsound import playsound
#pip install pyrebase4




listener = sr.Recognizer()
engine = pyttsx3.init()

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

def obtener_info():
    try:
        with sr.Microphone() as source:
            playsound
            print('Escuchando...')
            listener.pause_threshold = 1
            listener.energy_threshold = 400
            voice = listener.listen(source)
            info= listener.recognize_google(voice,language='es-mx')
            print(info)
            return info.lower()
    except:
        pass
def enviar_datos():
        print('Hola')

def obtener_datos():
    hablar('nombre del contacto')
    nombre = obtener_info()
    hablar('cual es la terminacion del correo?')
    terminacioncorreo= obtener_info()
    if 'gmail' in terminacioncorreo or 'hotmail' in terminacioncorreo or 'outlook' in terminacioncorreo:
        hablar('Okay')
    hablar('diga el correo antes del arroba')
    correo=obtener_info()
    correo = correo.replace(' ','')
    correofull = correo + '@' + terminacioncorreo + '.com'
    print(correofull)
    subir_info(nombre,correofull)


def subir_info(nombre,correo):
    ref = db.reference('/Correos')
    datos = {'nombre':nombre,'correo':correo}
    ref.child(nombre).set(datos)
    hablar('el correo se agrego con exito')

def obtener_correo(nombre):
    ref =db.reference('/Correos/'+nombre+'/correo')
    resultado = ref.get()
    #resultado= ref.order_by_child("nombre").equal_to(nombre).get()
    print(resultado)
    return(resultado)


    



