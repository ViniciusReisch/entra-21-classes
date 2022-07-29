import pyautogui as pi
from time import sleep

pi.press('win')
pi.write('Chrome')
sleep(1)
pi.click(r'C:\Users\vinicius.reisch\PycharmProjects\pythonProject\pyautogui\Screenshot_8.png')
sleep(1)
pi.write('https://pt.wikipedia.org/wiki/Paradoxo_do_gato_e_pão_com_manteiga')
pi.press('enter')