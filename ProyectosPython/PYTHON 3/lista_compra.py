lista_supermercado = ["Pan", "Cebolla", "Pimienta"]
def lista_compra():
    lista_nueva = []
    print("Solo puedes ingresar los siguientes productos")
    print("\n".join(lista_supermercado))
    productos = None
    while productos not in lista_supermercado:
        productos = input("Ingrese un producto de la lista [q para salir]: ")
        if productos in lista_supermercado:
            lista_nueva.append(productos)
        elif productos == "q":
            break
    return print(lista_nueva)


def archivo_externo(nombre_archivo):
    archivo = open(nombre_archivo + ".txt", "w")
    archivo.write("\n".join(lista_supermercado))
    archivo.close()


def main():
    lista_compra()
    archivo_externo(input("Ingrese un nombre para su archivo: "))


if __name__ == "__main__":
    main()