import pyautogui as pi
from time import sleep

pi.press('win')
pi.write('Chrome')
sleep(1)
pi.click(515, 372)
sleep(1)
pi.write('https://externo.proway.com.br')
pi.press('enter')
sleep(2)
pi.click(r'C:\Users\vinicius.reisch\PycharmProjects\pythonProject\pyautogui\Screenshot_9.png')
email = pi.prompt('Email:')
pi.click(497, 375)
pi.write(email)
pi.click(500, 472)
senha = pi.password('Senha: ')
pi.write(senha)
pi.press('enter')