# (python text to speech) pyttsx3
import re

import pyttsx3
import speech_recognition
import speech_recognition as sr

#Iniciamos el motor
engine = pyttsx3.init()
#Con esta propiedad le damos la propiedad de velocidad de audio
engine.setProperty("rate", 130)
#Definimos las propiedades
engine.setProperty("voice", "spanish")
#El motor recibe lo escrito
engine.say("Hola, como te llamas")
#El motor reproduce el audio+
engine.runAndWait()

#sr = Speech Recognizer
# Reconoce una pista de audio y la identifica
r = speech_recognition.Recognizer()

# Abrimos un fichero virtual y se guarda lo que hablamos
with sr.Microphone() as source:
    print("Puedes Hablar")
    # Escucha la fuente en la que se esta guardando la voz
    audio = r.listen(source)
    # Convertimos el reconocimiento en texto mediante Google
    text = r.recognize_google_cloud(audio, language="es-MX") # Damos como parametro la identificacion en español
    # Damos un parametro que filtre del texto entendido el nombre del usuario
    name = re.findall("me llamo ([A-Za-z]+)", text)
    # El ordenador te responde con el nombre identificado
    engine.say("Encantado de conocerte, {}".format(name[0]))
    engine.runAndWait()



    # VER VIDEO Y ARREGLAR PROBLEMA DE RECONOCIMIENTO DE VOZ
    # r.recognize_google_cloud(audio, language="es-MX") PROBLEMA