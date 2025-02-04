import uiautomator2 as u2
import time
import os
import threading

carreraTomada = False

def buscar_y_clicar_texto(texto):
    d = u2.connect()
    if d(textContains=texto).exists():
        d.click(530, 470)
        time.sleep(0.2)

time.sleep(7)

while not carreraTomada:
    try:
        buscar_y_clicar_texto("metro")
        time.sleep(0.3)
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        break
