import random

VIDA_POKEMON = 100
PORCENTAJE_VIDA = 10


# Pokemon Enemigo Aleatorio
eleccion_pokemon = random.randint(1, 5)
if eleccion_pokemon == 1:
    pokemon_cpu = "Bulbasaur"
elif eleccion_pokemon == 2:
    pokemon_cpu = "Beedrill"
elif eleccion_pokemon == 3:
    pokemon_cpu = "Charmander"
elif eleccion_pokemon == 4:
    pokemon_cpu = "Psyduck"
elif eleccion_pokemon == 5:
    pokemon_cpu = "Pikachu"

print("\nEl pokemon contrario es " + pokemon_cpu + "\n")

# Eleccion Pokemon Usuario
eleccion_usuario = None
while eleccion_usuario != 1 and eleccion_usuario != 2 and eleccion_usuario != 3 and eleccion_usuario != 4 and eleccion_usuario != 5:
    print("1: Bulbasaur\n"
          "2: Beedrill\n"
          "3: Charmander\n"
          "4: Psyduck\n"
          "5: Pikachu")
    eleccion_usuario = int(input("Escoge un personaje [1, 2, 3, 4, 5] "))

if eleccion_usuario == 1:
    pokemon_usuario = "Bulbasaur"
elif eleccion_usuario == 2:
    pokemon_usuario = "Beedrill"
elif eleccion_usuario == 3:
    pokemon_usuario = "Charmander"
elif eleccion_usuario == 4:
    pokemon_usuario = "Psyduck"
elif eleccion_usuario == 5:
    pokemon_usuario = "Pikachu"

print("Tu pokemon es {}".format(pokemon_usuario))
print("\n\n")

print("La vida de tu pokemon {} es de {}." .format(pokemon_usuario, VIDA_POKEMON))
print("[{}]".format("#"*PORCENTAJE_VIDA))
print("La vida del pokemon contrario {} es de {}." .format(pokemon_cpu, VIDA_POKEMON))
print("[{}]".format("#"*PORCENTAJE_VIDA))
print("\n\n")

vida_pokemom_usuario = VIDA_POKEMON
vida_pokemom_cpu = VIDA_POKEMON
while vida_pokemom_usuario > 0 and vida_pokemom_cpu > 0:
    # Batalla

    # Ataque Cpu
    ataque_pok_cpu = random.randint(1, 3)

    if ataque_pok_cpu == 1:
        print("{} ataco con golpe certero.".format(pokemon_cpu))
        vida_pokemom_usuario -= 10
    elif ataque_pok_cpu == 2:
        print("{} ataco con ataque directo.".format(pokemon_cpu))
        vida_pokemom_usuario -= 12
    elif ataque_pok_cpu == 3:
        print("{} ataco con ataque especial.".format(pokemon_cpu))
        vida_pokemom_usuario -= 15

    # Ataque Usuario
    ataque_usuario = None
    while ataque_usuario != 1 and ataque_usuario != 2 and ataque_usuario != 3:
        print("1: Ataque Certero\n"
              "2: Ataque Directo\n"
              "3: Ataque Especial")
        ataque_usuario = int(input("¿Que ataque deseas realizar? [1, 2, 3] "))

    if ataque_usuario == 1:
        print("Hiciste 10 de daño a {}".format(pokemon_cpu))
        vida_pokemom_cpu -= 10
    elif ataque_usuario == 2:
        print("Hiciste 12 de daño a {}".format(pokemon_cpu))
        vida_pokemom_cpu -= 12
    elif ataque_usuario == 3:
        print("Hiciste 15 de daño a {}".format(pokemon_cpu))
        vida_pokemom_cpu -= 15

    if vida_pokemom_cpu < 0:
        vida_pokemom_cpu = 0
        break
    elif vida_pokemom_usuario < 0:
        vida_pokemom_usuario = 0
        break

    porcentaje_vida_usuario = int((PORCENTAJE_VIDA*vida_pokemom_usuario/VIDA_POKEMON))
    porcentaje_vida_cpu = int((PORCENTAJE_VIDA*vida_pokemom_cpu/VIDA_POKEMON))
    print("La vida de tu pokemon {} es {}".format(pokemon_usuario, vida_pokemom_usuario))
    print("[ {} ]".format("#"*porcentaje_vida_usuario))
    print("La vida del pokemon contrario {} es {}".format(pokemon_cpu, vida_pokemom_cpu))
    print("[ {} ]".format("#"*porcentaje_vida_cpu))

print("\n\n")

if vida_pokemom_cpu == 0:
    print("Eres el Ganadooor!!!")
elif vida_pokemom_usuario == 0:
    print("Has Perdidoooo!!!")