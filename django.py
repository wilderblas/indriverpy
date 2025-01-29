import uiautomator
import subprocess
import time

carreraTomada = False

def buscar_texto_y_click(texto_buscar):
    # Conectar al dispositivo usando ADB
    device = uiautomator.Device()

    # Buscar el texto en la pantalla
    elements = device(text=texto_buscar)

    if elements.exists:
        # Si encontramos el texto, obtener las coordenadas de la posición
        for element in elements:
            bounds = element.bounds
            print(f"Texto '{texto_buscar}' encontrado en las coordenadas: {bounds}")
            # Hacer click en las coordenadas encontradas (el punto central del área)
            click_x = (bounds['left'] + bounds['right']) / 2
            click_y = (bounds['top'] + bounds['bottom']) / 2

            # Ejecutar el comando ADB para hacer click usando las coordenadas
            subprocess.run(["adb", "shell", f"input tap {int(click_x)} {int(click_y)}"])

            print(f"Hicimos click en las coordenadas ({int(click_x)}, {int(click_y)})")
            return

    print(f"No se encontró el texto '{texto_buscar}' en la pantalla.")

# Llamar la función con el texto que deseas buscar y hacer click
subprocess.run(["termux-wake-lock"])

device = uiautomator.Device()  # Crear la instancia una vez fuera del bucle

while not carreraTomada:
    try:
        elements = device(text="metro")
        if elements.exists:
          subprocess.run(["adb", "shell", "input tap 540 460"])
          print("Se hizo click")
        time.sleep(1)
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        break

