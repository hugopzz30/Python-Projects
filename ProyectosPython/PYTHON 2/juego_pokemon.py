import os
import random
import readchar

#Mapa
map_definition = """\
###                 ###              ####
######             ##    ##              #
##             ##           ### #      ##
####                 ####              ###
     #####                    ####       #
###                 ###                   ##
        ###                    ###          #
###                        ##          ##
#                 ###    #                 ##\
"""

map_definition = [list(row) for row in map_definition.split("\n")]

#Constantes
POS_X = 0
POS_Y = 1

# Tamaño Mapa
MAP_WIDTH = len(map_definition[0])
MAP_HEIGHT = len(map_definition)

#Variables

#Variable Posicion
my_position = [random.randint(1, MAP_WIDTH - 1), random.randint(1, MAP_HEIGHT - 1)]

# Variables Juego Pokemon
trainers = 4
trainers_position = []
NUM_POKEMONES = [1, 2, 3, 4, 5]
eleccion_pokemon = None
POKEMON_LIFE = 100
user_pokemons_life = 100
cpu_pokemon_life = 100
USER_LIFE_BAR = int((user_pokemons_life * 10) / POKEMON_LIFE)
PRIMARY_ATTACK = 10
SECONDARY_ATTACK = 20
ULTIMATE = 30

# Eleccion Pokemon
while eleccion_pokemon not in NUM_POKEMONES:
    eleccion_pokemon = int(input ("""Escoge un pokemon [Ingrese un numero]
1: Pikachu
2: Bulbasaur
3: Squirtle
4: Charmander
5: Psyduck
: """))

    if eleccion_pokemon == 1:
        pokemon_usuario = "Pikachu"
    elif eleccion_pokemon == 2:
        pokemon_usuario = "Bulbasaur"
    elif eleccion_pokemon == 3:
        pokemon_usuario = "Squirtle"
    elif eleccion_pokemon == 4:
        pokemon_usuario = "Charmander"
    elif eleccion_pokemon == 5:
        pokemon_usuario = "Psyduck"


# Aparicion de entrenadores
while trainers > len(trainers_position):
    new_position = [random.randint(1, MAP_WIDTH - 1), random.randint(1, MAP_HEIGHT - 1)]

    if new_position != my_position and new_position not in trainers_position\
            and map_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
        trainers_position.append(new_position)


# Inicio Juego

end_game = False
fight = False

while not end_game:
    os.system("cls")

    print("\t\tPUEBLO LAVANDA")
    print("\nTu pokemon es {} tienes {} de vida ".format(pokemon_usuario, user_pokemons_life))
    print("\t\t[{}]" .format("#" * USER_LIFE_BAR))

    print("+" + "-" * MAP_WIDTH + "+")
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end = "")
        random_cpu_pokemon = None

        # Batalla Pokemon
        if fight == True:
            print("\n\n¡¡¡BIENVENIDO A LA ZONA DE PELEA!!!")

            if pokemon_usuario != "Psyduck":
                random_cpu_pokemon = random.randint(1, 4)
                while user_pokemons_life > 0 and cpu_pokemon_life > 0:

                    if random_cpu_pokemon == 1:
                        cpu_pokemon = "Pikachu"
                    elif random_cpu_pokemon == 2:
                        cpu_pokemon = "Bulbasaur"
                    elif random_cpu_pokemon == 3:
                        cpu_pokemon = "Squirtle"
                    elif random_cpu_pokemon == 4:
                        cpu_pokemon = "Charmander"

                    print("El pokemon enemigo es {}".format(cpu_pokemon))

                    print("\n\n¡¡¡QUE COMIENCE LA BATALLA !!!")

                    cpu_attack = random.randint(1, 3)
                    if cpu_attack == 1:
                        user_pokemons_life -= PRIMARY_ATTACK
                        cpu_attack = "ataque primario"
                    elif cpu_attack == 2:
                        user_pokemons_life -= SECONDARY_ATTACK
                        cpu_attack = "ataque secundario"
                    elif cpu_attack == 3:
                        user_pokemons_life -= ULTIMATE
                        cpu_attack = "ataque final"

                    print("{} realizo un {}, tienes {} de vida. ".format(cpu_pokemon, cpu_attack,
                                                                         user_pokemons_life))

                    user_attack = None
                    attacking_options = [1, 2, 3]

                    while user_attack not in attacking_options:
                        user_attack = int(input("Elige que ataque realizar\n"
                                                "1: Ataque Primario\n"
                                                "2: Ataque Secundario\n"
                                                "3: Ataque Final\n"
                                                "[1, 2, 3] "))

                        if user_attack == 1:
                            cpu_pokemon_life -= PRIMARY_ATTACK
                        elif user_attack == 2:
                            cpu_pokemon_life -= SECONDARY_ATTACK
                        elif user_attack == 3:
                            cpu_pokemon_life -= ULTIMATE

                    if cpu_pokemon_life < 0 and user_pokemons_life < 0:
                        user_pokemons_life = 0
                        cpu_pokemon_life = 0

                    USER_LIFE_BAR = int((user_pokemons_life * 10) / POKEMON_LIFE)
                    CPU_LIFE_BAR = int((cpu_pokemon_life * 10) / POKEMON_LIFE)

                    if cpu_pokemon_life <= 0:
                        print("{} ¡¡¡HAS GANADO!!!".format(pokemon_usuario))
                    elif user_pokemons_life <= 0:
                        print("{} ¡¡¡HAS PERDIDO!!!".format(cpu_pokemon))

                    print("{} [ {} ] {}/{}".format(pokemon_usuario, "#" * USER_LIFE_BAR, user_pokemons_life,
                                                   POKEMON_LIFE))
                    print("{} [ {} ] {}/{}".format(cpu_pokemon, "#" * CPU_LIFE_BAR, cpu_pokemon_life, POKEMON_LIFE))

                    # Volver a moverse dentro de mapa


            else:
                print("¡¡¡Has ganado todas las batallas, Psyduck no tiene competencia")

            break

        # Movimiento / Mapa
        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            fight_zone = None

            for trainer in trainers_position:

                if trainer[POS_X] == coordinate_x and trainer[POS_Y] == coordinate_y:
                    char_to_draw = "?"
                    fight_zone = trainer

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw= "^"

                if fight_zone:
                    trainers_position.remove(fight_zone)
                    fight = True

            if map_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"


            print("{}" .format(char_to_draw), end = "")


        print("|")
    print("+" + "-" * MAP_WIDTH + "+")


    # Movimiento

    print("[wasd] to move [q] to quit")

    direction = readchar.readchar()
    new_position = None


    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]
    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]
    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "q":
        end_game = True

    if new_position:
        if map_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position





