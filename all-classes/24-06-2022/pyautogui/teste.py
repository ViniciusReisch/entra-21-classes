import pyautogui as pi
from time import sleep

pi.press('win')
sleep(1)
pi.write('chrome')
sleep(1)
pi.press('enter')
sleep(1)
pi.click(175, 48)
sleep(1)
pi.write('https://web.whatsapp.com/')
pi.press('enter')
sleep(15)
pi.click(286,371)
sleep(1)
pi.write('Oi. Eu, Vinicius, estou aprendendo a usar o pyautogui')
pi.press('enter')