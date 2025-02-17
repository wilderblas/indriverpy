import keyboard
import uiautomator2 as u2
import time
import os

time.sleep(8)

print("Presiona W, A, S, D o X para ejecutar una acción. Presiona 'Esc' para salir.")

# Mapeo de teclas a acciones
acciones = {
    "W": print("Aceptar"),
    "A": print("Opcion1"),
    "S": print("Opcion2"),
    "D": print("Opcion3"),
    "X": print("Cerrar")
}

while True:
    event = keyboard.read_event()  # Espera a que se presione una tecla
    if event.event_type == keyboard.KEY_DOWN:  # Solo detecta cuando la tecla se presiona
        key = event.name.upper()  # Convierte la tecla a mayúscula

        if key in acciones:
            acciones[key]  # Imprime la acción correspondiente
        elif key == "ESC":  # Si presiona "Escape", sale del programa
            print("Saliendo...")
            break
