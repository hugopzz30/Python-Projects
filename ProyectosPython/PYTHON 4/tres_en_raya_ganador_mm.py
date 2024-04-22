# TAREAS

# CONVERTIRLO EN PROGRMACION FUNCIONAL
# BOTON PARA REINICIAR LA PARTIDA
# TEXTO AL MOMENTO DE GANAR

import PySimpleGUI as sg


PLAYER_ONE = "X"
PLAYER_TWO = "O"

# Jugador por Default
current_player = PLAYER_ONE


# Tablero 3 en raya [ 0 al 8 ]
deck = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]

# Guardamos las jugadas ganadoras
winner_plays = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
               [0, 3, 6], [1, 4, 7], [2, 5, 8],
               [0, 4, 8], [2, 4, 6]]

# Tamaño de los botones
button_size = (7, 3)

# key = "-1-" Esto es un identificador de las tuplas

# Lista de elemntos en nuestra ventana
# Las claves o llaves deben coincidir con deck
layout = [[sg.Button("", key="-0-", size=button_size),
           sg.Button("", key="-1-", size=button_size), # 1 FILA
           sg.Button("", key="-2-", size=button_size)],

           [sg.Button("", key="-3-", size=button_size),
            sg.Button("", key="-4-", size=button_size), # 2 FILA
            sg.Button("", key="-5-", size=button_size)],

            [sg.Button("", key="-6-", size=button_size),
            sg.Button("", key="-7-", size=button_size), # 3 FILA
            sg.Button("", key="-8-", size=button_size)],

            # Avisar quien ha ganado y quien ha perdido
            [sg.Text("", key="WINNER")],

            [sg.Button("Salir del Juego", key="Finish")],
            # [sg.Input("", key="Formulario")]

          ]


# Nombre de la ventana abierta caracteristicas
window = sg.Window("DEMO", layout, margins=(100, 100))
game_end = False

# PARA QUE EL PROGRAMA NO CIERRE, USAMO UN BUCLE
while True:
    # Tupla de la interfaz
    event, values = window.read()

    # Si clickeamos los botones de cerrar o 'Salir del Juego', se cierra el juego
    if event == "Finish" or event == sg.WIN_CLOSED:
        break


    # Bloqueamos los elementos 'X' o 'O' para que no puedan ser modificados
    # Si el boton esta en blanco, MARCALO
    if window.Element(event).ButtonText == "" and not game_end == True:
        # Convertimos en entero las llaves
        index = int(event.replace("-", ""))
        # En la posicion de la tabla deck que representa el tablero colocamos 'X' o 'O'
        # Replica del tablero en una lista
        deck[index] = current_player
        # Colocamos 'X' o 'O' encima de los botones
        window.Element(event).Update(text=current_player)

    for winner_play in winner_plays:
        # Con las jugadas guardadas, se compara con las posiciones del deck
        # Las jugadas ganadoras se van comparando con las posiciones dentro del deck
        # Si existe una combinacion ganadora dentro del deck, en la cual todos los elementos en las
        # posiciones coinciden con una combinacion, existe un ganador

        # Si la posicion ganadora dentro del deck es diferente de cero
        if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] != 0:

           # Si una combinacion ganadora es de 'X' o 'O', entra
            if deck[winner_play[0]] == PLAYER_ONE:
                print("El jugador 1 a ganado!!")
            else:
                print("El jugador 2 a ganado!!")

            # Si el juego no ha terminado sigue el juego, aun se pueden modificar las casillas
            game_end = True


    # Si nadie gana
    if 0 not in deck:
        # COLOCAR EN LA INTERFAZ (TAREA)
        print("JUEGO TERMINADO!!! NADIE HA GANADO")
        game_end = True


    # Intercambiamos de jugador cada que coloquemos 'X' o 'O'
    if current_player == PLAYER_ONE:
        current_player = PLAYER_TWO
    else:
        current_player = PLAYER_ONE

window.close()