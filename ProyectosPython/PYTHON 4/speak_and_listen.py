import pyttsx3
# import speech_recognition

engine = pyttsx3.init()
engine.setProperty("rate", 200)
engine.setProperty("voice", "spanish")
engine.setProperty()

# r = speech_recognition.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()


"""def hear_me():
    with (speech_recognition.Microphone() as source):
        print("Escuchando...")
        audio = r.listen(source)

        try:
            text = r.recognize_google_cloud(audio, language="es-ES")
            print("He entendido: {}".format(text))
            return text
        except speech_recognition.UnknownValueError:
            return None

"""

# Este codigo solo se ejecuta si el archivo se esta ejecutando como fuente principal
if __name__ == "__main__":
    speak("TU PUTA MADRE")
    #hear_me()