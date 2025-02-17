import uiautomator2 as u2
import time
import sys
import tty
import termios
import os
import select
#import threading

#carreraTomada = False
def leer_tecla(timeout=7):
    """Lee una sola tecla sin necesidad de presionar Enter, con un tiempo de espera."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        # Espera hasta `timeout` segundos por la entrada del usuario
        rlist, _, _ = select.select([sys.stdin], [], [], timeout)
        if rlist:
            return sys.stdin.read(1).upper()  # Captura un solo carácter y lo convierte a mayúscula
        else:
            return None  # Si no hay entrada, devuelve None
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

while True:
    try:
        d = u2.connect()
        if d(textContains="Ofrece tu tarifa").exists():
            os.system("mpv sonido.mp3")
            d.click(715,1298)
            key = leer_tecla(timeout=7)  # Espera 7 segundos por una tecla
            if key == "W":
                print("Aceptar")
                #break
            elif key == "A":
                print("Opcion1")
                #break
            elif key == "S":
                print("Opcion2")
                #break
            elif key == "D":
                print("Opcion3")
                #break
            elif key == "X":
                print("Cerrar")
                #break
            elif key == "Q":  # Presionar "Q" para salir
                print("Saliendo...")
                #break
            time.sleep(3)
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        break