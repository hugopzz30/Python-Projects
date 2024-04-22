import random
from requests_html import HTMLSession
from PIL import Image
from io import BytesIO
# from speak_and_listen import speak, hear_me

# DEJA EL CODIGO SIEMPRE MEJOR DE LO QUE TE LO ENCONTRASTE

def main():
    #speak("Bienvenido al precio justo, vamos a intentar adivinar los precios de algunos productos")
    session = HTMLSession()
    main_site = session.get("https://www.elpalaciodehierro.com/") #Entramos mediante codigo a la pagina web
    categories = main_site.html.find(".b-categories_navigation-link_3") #Obtenemos en una lista las categorias que existen
    category = random.choice(categories) # random.choice : Escoge un random en una lista

    # Si queremos descartar una opcion dentro de la lista de categorias usamos...
    #while category.text == "Nombre_a_descartar":
        #category = random.choice(categories)

    product_page = session.get(category.attrs["href"]) #Obtenemos el link del producto, el cual se encuentra en el diccionario
    products = product_page.html.find(".m-type_4")
    product = random.choice(products)


    product_link =  product.absolute_links #Cuando solo hay un objeto se llama directamente
    product_brand = product.find(".b-product_tile-brand", first=True).text #Filtra el objeto y devuelve el texto del producto
    product_title = product.find(".b-product_tile-name", first=True).text
    product_price = product.find(".b-product_price-value", first=True).text
    product_img = product.find(".h-blend_mode_img", first=True).attrs["data-src"]

    # Obtenemos la imagen
    img = session.get(product_img)
    image = Image.open(BytesIO(img.content))
    image.show()


    print(product_link)
    print(product_brand)
    print(product_title)
    print(product_price)

if __name__ == "__main__":
    main()



# TAREA
#Compara el user_guess con el precio del producto
#Haz que el juego sea para dos jugadores y que cada uno pueda adivinar el precio del producto. Gana el jugador que diga el precio más cercano al original. El juego debe tener 5 rondas y como hemos dicho, dos jugadores. ¡GO!
#Permite que el usuario escoja la categoría, permite la elección entre 5 categorías diferentes.