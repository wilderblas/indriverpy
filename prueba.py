from uiautomator import Device
import time

# Conectar con el dispositivo (asegúrate de que tu dispositivo esté conectado y en modo depuración)
d = Device()

# Coordenadas donde quieres hacer clic
x = 500
y = 600
time.sleep(5)
# Simular el clic en las coordenadas (x, y)
d.click(x, y)
print(f"Clic simulado en las coordenadas ({x}, {y})")
time.sleep(0.5)
d.click(x, y)
print(f"Clic simulado en las coordenadas ({x}, {y})")
time.sleep(0.5)
d.click(x, y)
print(f"Clic simulado en las coordenadas ({x}, {y})")
time.sleep(0.5)
d.click(x, y)
print(f"Clic simulado en las coordenadas ({x}, {y})")
time.sleep(0.5)