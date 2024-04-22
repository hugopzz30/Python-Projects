from time import sleep
#from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

#Otra forma de buscar elementos es por la libreria HTMLSession
"""
session = HTMLSession()
page_content = session.get(url)
"""


URL = "https://www.cyberpuerta.mx/"
driver = webdriver.Firefox()

def set_driver (url):
    driver.get(url)


def action_move_to_element (element):
    action = ActionChains(driver)
    action.move_to_element(element).perform()
    sleep(2)


def find_element_sendkeys(BY_ID, name_id, key):
    driver.find_element(BY_ID, name_id).send_keys(key)


def find_element_click(BY_ID, name_id):
    driver.find_element(BY_ID, name_id).click()


def find_element(BY_ID, name_id):
    element_found = driver.find_element(BY_ID, name_id)
    return element_found



def main ():
    set_driver(URL)
    action_move_to_element(find_element(By.CLASS_NAME, "oxwidget_headerlogin_title1 "))
    find_element_sendkeys(By.ID, "loginEmail", "hugo.peror.04@gmail.com")
    find_element_sendkeys(By.ID, "loginPassword", "Jabulani301@")
    find_element(By.CLASS_NAME, "oxwidget_headerlogin_popup")
    find_element(By.TAG_NAME, "form")
    find_element_click(By.XPATH, "//div[@class='oxwidget_headerlogin_popup']//form"
                                                           "//li[@class='formSubmit']//button")


if __name__ == '__main__':
    main()