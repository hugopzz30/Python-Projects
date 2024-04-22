
def long_word():
    lista_palabras = ["como", "hipopotamo", "elefante", "perros"]
    resultado = max(lista_palabras, key=len)
    print("La palabra más larga es {}".format(resultado))
    return resultado

def suma():
    lista_numeros = [1, 5, 9, 15, 42, 74, 11]
    resultado = 0
    for a in lista_numeros:
        resultado += a
    print("La suma de los numeros en lista es {}".format(resultado))
    return resultado

def par_impar(numero):
    fal_ver = None
    if (numero % 2) == 0:
        fal_ver = False
    else:
        fal_ver = True
    return print(fal_ver)


def seguro():
    print("¿Te quiere?")
    decision = input("")
    conf = None
    if decision == "si":
        confirmacion = input("Seguro?? [si / no]")
        if confirmacion == "si":
            conf = True
        elif confirmacion == "no":
            conf = False
    elif decision == "no":
        confirmacion = input("Seguro?? [si / no]")
        if confirmacion == "si":
            conf = False
        elif confirmacion == "no":
            conf = True
    return print(conf)


def mayus():
    cadena = input("Ingresa una cadena: ")
    cadena_mayus = ""
    for char in cadena:
        if 'a' <= char <= 'z':
            # Convertir el caracter a mayúscula sumándole la diferencia entre 'a' y 'A'
            char = chr(ord(char) - ord('a') + ord('A'))
        cadena_mayus += char
    print("La palabra en mayusculas es: {}".format(cadena_mayus))


def adivina(numero):
    num_usuario = 0
    while num_usuario != numero:
        num_usuario = int(input("Ingresa un numero entre 1 y 100: "))
    if num_usuario == numero:
        print("Lo encontraste")

lista_compra = ['leche', 'queso', 'tomate']
def compras():
    salir = True
    while salir:
        deseos = input("[q para salir] Que desea agregar en su lista: ")
        if deseos in lista_compra:
            print("Este item ya se encuentra en la lista")
        elif deseos == "q":
            salir = False
        else:
            lista_compra.append(deseos)
    return print(lista_compra)





def main():
    long_word()
    suma()
    par_impar(8)
    seguro()
    mayus()
    adivina(54)
    compras()


if __name__ == "__main__":
    main()