from math import inf
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
import datos


listener = sr.Recognizer()
engine = pyttsx3.init()

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

def obtener_info():
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            listener.pause_threshold = 1
            listener.energy_threshold = 400
            voice = listener.listen(source)
            info= listener.recognize_google(voice,language='es-mx')
            print(info)
            return info.lower()
    except:
        pass
def enviar_correo(receptor,asunto,mensaje):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('asistentepersonal26@gmail.com','IDAN0p0dras')
        email = EmailMessage()
        email['From'] = 'asistentepersonal26@gmail.com'
        email['To'] = receptor
        email['Subject'] = asunto
        email.set_content(mensaje)
        server.send_message(email)
        

def obtener_info_emails():
    hablar('¿A quien le quieres enviar el correo?')
    nombre = obtener_info()
    receptoremail = datos.obtener_correo(nombre)
    print(receptoremail)
    hablar('¿Cual es el asunto de su email?')
    asunto = obtener_info()
    hablar('¿Que quiere decir en su mail?')
    mensaje = obtener_info()
    enviar_correo(receptoremail,asunto,mensaje)
    hablar('Tu correo a sido enviado')
    hablar('¿Quieres enviar otro correo?')
    enviar_otro=obtener_info()
    if 'sí' in enviar_otro:
        obtener_info_emails()




