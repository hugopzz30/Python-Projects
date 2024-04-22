# TAREA: ANALIZAR CUANDO ALGUIEN HA GANADO EL JUEGO


import PySimpleGUI as sg


PLAYER_ONE = "X"
PLAYER_TWO = "O"

current_player = PLAYER_ONE

# Tamaño de los botones
button_size = (7, 3)

# key = "-1-" Esto es un identificador de las tuplas


# Combinaciones posibles
# NO SIRVEEEEEE
COMBINATIONS = [["-1-", "-2-", "-3-"], ["-1-", "-3-", "-2-"], ["-2-", "-1-", "-3-"], ["-2-", "-3-", "-1-"], ["-3-", "-1-", "-2-"], ["-3-", "-2-", "-1-"],
                ["-4-", "-5-", "-6-"], ["-4-", "-6-", "-5-"], ["-5-", "-4-", "-6-"], ["-5-", "-6-", "-4-"], ["-6-", "-5-", "-4-"], ["-6-", "-4-", "-5-"],
                ["-7-", "-8-", "-9-"], ["-7-", "-9-", "-8-"], ["-8-", "-7-", "-9-"], ["-8-", "-9-", "-7-"], ["-9-", "-8-", "-7-"], ["-9-", "-7-", "-8-"],
                ["-1-", "-4-", "-7-"], ["-1-", "-7-", "-4-"], ["-4-", "-1-", "-7-"], ["-4-", "-7-", "-1-"], ["-7-", "-1-", "-4-"], ["-7-", "-4-", "-1-"],
                ["-2-", "-5-", "-8-"], ["-2-", "-8-", "-5-"], ["-5-", "-2-", "-8-"], ["-5-", "-8-", "-2-"], ["-8-", "-2-", "-5-"], ["-8-", "-5-", "-2-"],
                ["-3-", "-6-", "-9-"], ["-3-", "-9-", "-6-"], ["-6-", "-3-", "-9-"], ["-6-", "-9-", "-3-"], ["-9-", "-3-", "-6-"], ["-9-", "-6-", "-3-"],
                ["-1-", "-5-", "-9-"], ["-1-", "-9-", "-5-"], ["-5-", "-1-", "-9-"], ["-5-", "-9-", "-1-"], ["-9-", "-1-", "-5-"], ["-9-", "-5-", "-1-"],
                ["-3-", "-5-", "-7-"], ["-3-", "-7-", "-5-"], ["-5-", "-3-", "-7-"], ["-5-", "-7-", "-3-"], ["-7-", "-3-", "-5-"], ["-7-", "-5-", "-3-"]]


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

# Registramos los movimientos de los jugadores
movimientos_player_one = []
movimientos_player_two = []


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
        movimientos_player_one.append(event)
        current_player = PLAYER_TWO
    else:
        movimientos_player_two.append(event)
        current_player = PLAYER_ONE


    if movimientos_player_one in COMBINATIONS or movimientos_player_two in COMBINATIONS:
        window.close()

window.close()