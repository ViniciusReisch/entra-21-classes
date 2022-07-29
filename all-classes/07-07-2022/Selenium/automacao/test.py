from time import sleep
from selenium import webdriver


navegador = webdriver.Chrome()
navegador.get('https://google.com')
sleep(5)
navegador.find_element('name', 'q').send_keys('TEste').key