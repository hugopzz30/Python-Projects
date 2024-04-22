# TAREA: ANALIZAR CUANDO ALGUIEN HA GANADO EL JUEGO


import PySimpleGUI as sg


PLAYER_ONE = "X"
PLAYER_TWO = "O"

current_player = PLAYER_ONE

# Tamaño de los botones
button_size = (7, 3)

# key = "-1-" Esto es un identificador de las tuplas

# Lista de elemntos en nuestra ventana
layout = [[sg.Button("", key="-1-", size=button_size),
           sg.Button("", key="-2-", size=button_size), # 1 FILA
           sg.Button("", key="-3-", size=button_size)],

           [sg.Button("", key="-4-", size=button_size),
            sg.Button("", key="-5-", size=button_size), # 2 FILA
            sg.Button("", key="-6-", size=button_size)],

            [sg.Button("", key="-7-", size=button_size),
            sg.Button("", key="-8-", size=button_size), # 3 FILA
            sg.Button("", key="-9-", size=button_size)],

            [sg.Button("Salir del Juego", key="Finish")],
            # [sg.Input("", key="Formulario")]

          ]


# Nombre de la ventana abierta caracteristicas
window = sg.Window("DEMO", layout, margins=(100, 100))


# PARA QUE EL PROGRAMA NO CIERRE, USAMO UN BUCLE
while True:
    # Tupla de la interfaz
    event, values = window.read()

    # Si clickeamos los botones de cerrar o 'Salir del Juego', se cierra el juego
    if event == "Finish" or event == sg.WIN_CLOSED:
        break


    # Bloqueamos los elementos 'X' o 'O' para que no puedan ser modificados
    # Si el boton esta en blanco, MARCALO
    if window.Element(event).ButtonText == "":
        # Colocamos 'X' o 'O' encima de los botones
        window.Element(event).Update(text=current_player)


    # Intercambiamos de jugador cada que coloquemos 'X' o 'O'
    if current_player == PLAYER_ONE:
        current_player = PLAYER_TWO
    else:
        current_player = PLAYER_ONE

window.close()