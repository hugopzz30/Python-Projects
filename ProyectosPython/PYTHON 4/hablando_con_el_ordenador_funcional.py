# (python text to speech) pyttsx3
import re
import pyttsx3
import speech_recognition as sr

def initialize_engine():
    engine = pyttsx3.init()
    engine.setProperty("rate", 130)
    engine.setProperty("voice", "spanish")
    return engine


def recognize_voice(r):
    with sr.Microphone() as source:
        print("Puedes Hablar")
        audio = r.listen(source)
        text = r.recognize_google_cloud(audio, language="es_MX")
    return text

def identify_name(text):
    name = None
    # Buscamos ciertos patrones, asi tenemos diferentes casos
    patterns = ["me llamo ([A-Za-z]+)", "me nombre es ([A-Za-z]+)", "([A-Za-z]+)"]
    for pattern in patterns:
        # Usamos try cuando el usuario no da su nombre, si lo da retornamos el nombre
        try:
            name = re.findall(pattern, text)[0] # [0] Se usa porque el nombre lo estya guardando en una lista
        except IndexError:
            print("Pues... no ha dado el nombre")
    return name


def main():

    engine = initialize_engine()
    engine.say("Hola, como te llamas")
    engine.runAndWait()

    r = sr.Recognizer()

    text = recognize_voice(r)
    name = identify_name(text)

    if name:
        engine.say("Encantado de conocerte, {}".format(name))
    else:
        print("Pues miraaa, la verdad que no te entiendo....")
    engine.runAndWait()


if __name__ == "__main__":
    main()

