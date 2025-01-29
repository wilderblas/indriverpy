import uiautomator
import subprocess
import time
carreraTomada=False

def buscar_texto_y_click(texto_buscar):
    # Conectar al dispositivo usando ADB
    device = uiautomator.Device()

    # Definir las coordenadas de la parte de la pantalla donde se buscará el texto
    # Puedes ajustar las coordenadas según lo que necesites (ej: x1, y1 a x2, y2)
    x1, y1, x2, y2 = 0, 0, 1080, 1920  # Ajusta las coordenadas según la zona de búsqueda

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

while not carreraTomada:
  device=uiautomator.Device()
  elements = device(text="metro")

  if elements.exists:
    subprocess.run(["adb", "shell","input tap 540 460"])
    print("Se hizo click")
  time.sleep(1)
#buscar_texto_y_click("metro")
