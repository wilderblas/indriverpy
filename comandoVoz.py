import sys
import tty
import termios
import time

time.sleep(8)

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

print("Presiona W, A, S, D o X para imprimir un mensaje. Presiona 'Q' para salir.")

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

