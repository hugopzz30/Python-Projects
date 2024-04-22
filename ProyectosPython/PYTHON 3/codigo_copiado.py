SALIDA = "SALIR"
ARCHIVO_LISTA = "lista_compra.txt"

items_del_supermercado = ["pollo", "maiz", "lechuga", "pan"]

def preguntar_producto_usuario():
    return input("Introduce un producto [{} para salir]".format(SALIDA))

def guardar_lista_a_disco(lista_compra):
    nombre_fichero = input("Como quieres que se llame tu archivo? ")
    with open(ARCHIVO_LISTA, "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))


def guardar_item_en_lista(lista_compra, item_a_guardar):
    if item_a_guardar.lower() in [a.lower() for a in lista_compra]:
        print("El producto ya existe")
    else:
        lista_compra.append(item_a_guardar)

def cargar_o_crear_lista():
    lista_compra = []
    if input("¿Quieres cargar la ultima lista de la compra? [S/N]") == "S":
        try:
            with open(ARCHIVO_LISTA, "r") as a:
                lista_compra = a.read().split("\n")
        except FileNotFoundError:
            print("¡Archivo de la compra no encontrado!")
    return lista_compra


def mostrar_lista(lista_compra):
    print("\n".join(lista_compra))


def main():
    lista_compra = cargar_o_crear_lista()
    mostrar_lista(lista_compra)
    input_usuario = preguntar_producto_usuario()

    while input_usuario != SALIDA:
        guardar_item_en_lista(lista_compra, input_usuario)
        input_usuario = preguntar_producto_usuario()
    mostrar_lista(lista_compra)
    guardar_lista_a_disco(lista_compra)



if __name__ == "__main__":
    main()