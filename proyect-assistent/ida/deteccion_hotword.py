import os
import speech_recognition as sr


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
    
while True:
    
    consulta = hacercomando()
    
    if 'oye' in consulta:
        os.startfile('D:\\Documentos\\Proyecto\\rougue-studios\\proyect-assistent\\ida\\ida.py')
    else:
        print("Falsa alarma.......")