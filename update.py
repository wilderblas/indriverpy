import uiautomator2 as u2
import time
#import os
#import threading

d=u2.connect()

def buscar_y_clicar_texto(texto):
    if not d(textContains=texto).exists():
        d.swipe(500,350,500,1100,duration=0.03)

time.sleep(7)

while True:
    try:
        if d(text="Solicitudes de viaje").exists():
            buscar_y_clicar_texto("metro")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        break
