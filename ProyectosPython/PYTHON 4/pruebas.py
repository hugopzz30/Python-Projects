from time import sleep
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

url = "https://www.cyberpuerta.mx/"



driver = webdriver.Firefox()
driver.get(url)


# Estructurar Programa y Crear funciones


hover_option = driver.find_element(By.CLASS_NAME, "oxwidget_headerlogin_title1 ")
actions = ActionChains(driver)
actions.move_to_element(hover_option).perform()
sleep(2)


driver.find_element(By.ID, "loginEmail").send_keys("hugo.peror.04@gmail.com")
driver.find_element(By.ID, "loginPasword").send_keys("Jabulani301@")
(driver.find_element(By.CLASS_NAME, "oxwidget_headerlogin_popup").
 find_element(By.TAG_NAME, "form")).find_element(By.XPATH, "//div[@class='oxwidget_headerlogin_popup']//form"
                                                           "//li[@class='formSubmit']//button").click()