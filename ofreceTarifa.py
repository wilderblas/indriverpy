import uiautomator2 as u2
import time
import sys
import tty
import termios
import os
#import threading

#carreraTomada = False
def leer_tecla():
    """Lee una sola tecla sin necesidad de presionar Enter."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        tecla = sys.stdin.read(1)  # Lee un solo carácter
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return tecla

while True:
    try:
        d = u2.connect()
        if d(textContains="Ofrece tu tarifa").exists():
            os.system("mpv sonido.mp3")
            while True:
              key = leer_tecla().upper()  # Captura la tecla y la convierte a mayúscula

              if key == "W":
                  print("Aceptar")
              elif key == "A":
                  print("Opcion1")
              elif key == "S":
                  print("Opcion2")
              elif key == "D":
                  print("Opcion3")
              elif key == "X":
                  print("Cerrar")
              elif key == "Q":  # Presionar "Q" para salir
                  print("Saliendo...")
              break
            time.sleep(1)
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        break