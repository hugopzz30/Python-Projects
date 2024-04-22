from time import sleep

from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.by import By

url_cyberpuerta = "https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Tarjetas-de-Video/Tarjeta-de-Video-ASRock-AMD-Radeon-RX-6600-Challenger-D-OC-8GB-128-bit-GDDR6-PCI-Express-4-0.html"

session = HTMLSession()
page = session.get(url_cyberpuerta)
id_buy = page.html.find(".basketButton")


#Hacer Programa completo,

if len(id_buy) > 0:
    driver = webdriver.Edge()
    driver.get(url_cyberpuerta)
    sleep(2)
    driver.find_element(By.CLASS_NAME, "basketButton").find_element(By.TAG_NAME, "button").click()
    sleep(2)
    driver.find_element(By.CLASS_NAME, "clear").find_element(By.LINK_TEXT, "Ir a la caja").click()
    sleep(2)
    driver.find_element(By.CLASS_NAME, "clear embasket_nextstep_button").find_element(By.TAG_NAME, "button").click()


