from math import inf
from subprocess import TimeoutExpired
from firebase_admin import db
from email.message import EmailMessage
from playsound import playsound
import smtplib
import speech_recognition as sr
import pyttsx3
import datos



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
        playsound('D:\\Documentos\\Github\\Proyecto SOFTWARE\\rougue-studios\\resources\\SonidoIDA.mp3')
        audio = comando.listen(source,timeout=5)
        try:
            print("Entendiendo.......")
            consulta = comando.recognize_google(audio,language='es-mx')
            print(f"Dijiste: {consulta}")
            

        except Exception as Error:
            return "none"
        
        return consulta.lower()
        

        
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
        ref=db.reference('/calls/Emails/Enviados')
        resultado=ref.get()
        resultado = resultado +1
        ref=db.reference('/calls/Emails')
        ref.update({'Enviados':resultado})
        
def obtener_info_emails():
    habla('¿A quien le quieres enviar el correo?')
    nombre = hacercomando()
    if 'a' in nombre:
        habla('Diga solo el nombre a quien quiere enviar el correo porfavor')
        nombre=hacercomando()
        receptoremail = datos.obtener_correo(nombre)
        
    receptoremail = datos.obtener_correo(nombre)
    print(receptoremail)
    habla('¿Cual es el asunto de su email?')
    asunto = hacercomando()
    habla('¿Que quiere decir en su mail?')
    mensaje = hacercomando()
    enviar_correo(receptoremail,asunto,mensaje)
    habla('Tu correo a sido enviado')
    habla('¿Quieres enviar otro correo?')
    enviar_otro=hacercomando()
    if 'sí' in enviar_otro:
        obtener_info_emails()




