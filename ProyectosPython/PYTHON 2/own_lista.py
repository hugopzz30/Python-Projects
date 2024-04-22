lista_de_compra = []

answer = None
while answer != "Q":
    answer = input("¿Que deseas comprar hoy? [Q para salir]")
    if answer == "Q":
        break
    elif answer in lista_de_compra:
        print("{} ya esta en la lista".format(answer))
    else:
        user_choice = input("Seguro que desea agregar {} a su lista? [S / N]".format(answer))
        if user_choice == "S":
            lista_de_compra.append(answer)


print("\n\nSu lista de compras es:")
print(lista_de_compra)



