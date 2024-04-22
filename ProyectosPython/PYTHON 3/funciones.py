# Programacion Funcional

from time import sleep
# Biblioteca relacionada al tiempo
# sleep(seg)

# Ejemplo de una funcion
# Largo de un string
# Las variables dentro de una funcion solo existen en la funcion
def largo_string(mi_string):
    largo = 0
    for n in mi_string:
        largo += 1
    return largo

largo_de_string = largo_string("Hola Mundo")
print(largo_de_string)


def fibonacci_recursividad(n):
    if n <= 1:
        return 1
    return fibonacci_recursividad(n -1) + fibonacci_recursividad(n - 2)


def potencia(numero, base = 2): #Base 2 por defecto
    resultado = numero
    for a in range(1, base):
        resultado *= numero
    return resultado

def secuencia_fib (num):
    if (num == 0):
        return 0
    elif (num == 1):
        return 1
    else:
        return (secuencia_fib(num-2) + secuencia_fib(num-1)) #Retorna la suma de los dos numero anteriores


SALIDA = "Salir"

def preguntar_producto_usuario():
    return input("Introduce ubn producto [{} para salir]: ".format(SALIDA))


def compras():
    lista_compra = []
    input_usuario = preguntar_producto_usuario()

    while input_usuario != SALIDA:
        lista_compra.append(input_usuario)
        print("\n".join(input_usuario))
        input_usuario = input("Introduce un producto: ")

    a = open("compra.txt", "w")
    a.write("\n".join(lista_compra))
    a.close()

# En el mundo laboral se usa def main(): para crear codigo
def main():
    print("Hola Mundo")
    # pass se usa para correr codigo ignorando una funcion

    for a in range(10):
        print(fibonacci_recursividad(a))





# Por convencion para ejecutar la funcion main se usa:
if __name__ == "__main__":
    main()
    print(potencia(2, 4))
    print(potencia(6))
    # Se ejecuta main
