from playsound import playsound
import pyttsx3
import speech_recognition as sr

#<-------------------------------------------Funciones------------------------------------------->
Asistente = pyttsx3.init('sapi5')
voces = Asistente.getProperty('voices') #voices es el nombre de la propiedad, no se puede modificar 
Asistente.setProperty('voices',voces[0].id)
Asistente.setProperty('rate',150)

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
        
        except sr.TimeoutExpired as msg:
            print(msg)
                    
        except  sr.WaitTimeoutError as msg:
            print("El tiempo de espera ha terminado")
            quit()

        return consulta.lower() 
    
def Contestaciones():
    while True:
        consulta = hacercomando()   
        habla("Yo estoy muy bien y usted?")
        EstadoAnimo = hacercomando()
        if 'bien' in EstadoAnimo:
            habla('Me da mucho gusto , hay algo en lo que le pueda ayudar?')
            if 'si' in consulta:
                habla('En que le puedo ayudar?')
            if 'no' in consulta:
                habla('Nos vemos pronto!')
                break
        elif 'mal' in EstadoAnimo:
            habla('Que mal señor, me apena mucho, hay algo en lo que le pueda ayudar?')
            if 'si' in consulta:
                habla('En que le puedo ayudar?')
            if 'no' in consulta:
                habla('Nos vemos pronto!')
                break
        elif 'más o menos' in EstadoAnimo:
            habla('No entiendo a los humanos, son muy complejos, hay algo en lo que le pueda ayudar?')
            if 'si' in consulta:
                habla('En que le puedo ayudar?')
            if 'no' in consulta:
                habla('Nos vemos pronto!')
                break
        elif 'triste' in EstadoAnimo:
            habla('Me apena mucho que se sienta así, hay algo en lo que le pueda ayudar?')
            if 'si' in consulta:
                habla('En que le puedo ayudar?')
            if 'no' in consulta:
                habla('Nos vemos pronto!')
                break
        elif 'feliz' in EstadoAnimo:
            habla('¡Me alegra mucho!, hay algo en lo que le pueda ayudar?')
            if 'si' in consulta:
                habla('En que le puedo ayudar?')
            if 'no' in consulta:
                habla('Nos vemos pronto!')
                break
        elif 'asustado' in EstadoAnimo:
            habla('Cómase un pan para el susto, hay algo en lo que le pueda ayudar?')
            if 'si' in consulta:
                habla('En que le puedo ayudar?')
            if 'no' in consulta:
                habla('Nos vemos pronto!')
                break
        elif 'enojado' in EstadoAnimo:
            habla('Tranquilo señor, tómese un tiempo para pensar. Hay algo en lo que le pueda ayudar?')
            if 'si' in consulta:
                habla('En que le puedo ayudar?')
            if 'no' in consulta:
                habla('Nos vemos pronto!')
                break
        elif 'achicopalado' in EstadoAnimo:
            habla('Lo siento mucho, hay algo en lo que le pueda ayudar?')
            if 'si' in consulta:
                habla('En que le puedo ayudar?')
            if 'no' in consulta:
                habla('Nos vemos pronto!')
                break
       
def Triste():       
     while True:
        consulta = hacercomando()   
        habla('Me apena mucho que se sienta así, hay algo en lo que le pueda ayudar?')
        if 'si' in consulta:
                habla('En que le puedo ayudar?')
        if 'no' in consulta:
                habla('Nos vemos pronto!')
                break

def Feliz():       
    while True:
        consulta = hacercomando()   
        habla('Me alegra mucho, hay algo en lo que le pueda ayudar?')
        if 'si' in consulta:
                habla('En que le puedo ayudar?')
        if 'no' in consulta:
                habla('Nos vemos pronto!')
                break

def Enojado():       
    while True:
        consulta = hacercomando()   
        habla('Tómese unos minutos para tranquilizarse, hay algo en lo que le pueda ayudar?')
        if 'si' in consulta:
                habla('En que le puedo ayudar?')
        if 'no' in consulta:
                habla('Nos vemos pronto!')
                break

def Asustado():       
    while True:
        consulta = hacercomando()   
        habla('Échesé un pan pal susto, hay algo en lo que le pueda ayudar?')
        if 'si' in consulta:
                habla('En que le puedo ayudar?')
        if 'no' in consulta:
                habla('Nos vemos pronto!')
                break
