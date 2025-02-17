import uiautomator2 as u2
import time
import os
#import threading

#carreraTomada = False

time.sleep(7)

while True:
    try:
        d = u2.connect()
        if d(textContains="Ofrece tu tarifa").exists():
            os.system("mpv sonido.mp3")
            time.sleep(3)
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        break