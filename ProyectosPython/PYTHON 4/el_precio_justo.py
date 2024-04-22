#Importamos desde otro archivo una funcion
from speak_and_listen import speak, hear_me
import re

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
    speak("Hola, como te llamas")

    text = hear_me()
    name = identify_name(text)

    if name:
        speak("Encantado de conocerte, {}".format(name))
    else:
        speak("Pues miraaa, la verdad que no te entiendo....")

if __name__ == "__main__":
    main()
