from random import randint

vida_pikachu = 80
vida_squirtle = 90

while vida_pikachu > 0 and vida_squirtle > 0:
    # Se desenvuelven los turnos de combate

    # Turno de Pikachu # CPU
    print("Turno de Pikachu")
    ataque_pikachu = randint(1,2)
    if ataque_pikachu == 1:
        #Bola Voltio
        print("Pikachu ataca con vola Voltio")
        vida_squirtle -= 10
    else:
        print("Pikachu ataca con onda trueno")
        vida_squirtle -= 11

    print("La vida de Pikachu es: {}, la vida de Squirtle es: {}".format(vida_pikachu, vida_squirtle))

    input("Enter para continuar...\n\n")


    #Turno de Squirtle
    print("Turno de Squirtle")

    ataque_squirtle = None
    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B":
        ataque_squirtle = input("¿Que ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja: ")

    if ataque_squirtle == "P":
        print("Squirtle ataca con Placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Squirtle ataca con Pistola Agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja")
        vida_pikachu -= 9

    print("La vida de Pikachu es: {}, la vida de Squirtle es: {}".format(vida_pikachu, vida_squirtle))
    input("Enter para continuar... \n\n")

if vida_pikachu > vida_squirtle:
    print("Pikachu gana!")
else:
    print("Squirtle gana!")