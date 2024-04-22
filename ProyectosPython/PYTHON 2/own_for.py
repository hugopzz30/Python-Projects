largo_lista = int(input("Introduzca el largo de su lista: "))
lista_numeros = []
for n in range(largo_lista):
    numeros_lista =  int(input("Introduzca el dato {}: ".format(n+1)))
    lista_numeros.append(numeros_lista)

puntero = lista_numeros[0]
for num in lista_numeros:
    if puntero > num:
        numero_menor = num
    if puntero < num:
        numero_mayor = num

print("El numero mayor de la lista es {} ".format(numero_mayor))
print("El numero menor de la lista es {} ".format(numero_menor))
