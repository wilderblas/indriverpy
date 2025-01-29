import uiautomator2 as u2
import time

# Conectar con el dispositivo (asegúrate de que tu dispositivo esté conectado y en modo depuración)
d = u2.connect()

# Verifica que la conexión funciona
print(d.info)

# Coordenadas del clic
x, y = 500, 600
time.sleep(5)

# Simula clics
for i in range(4):
    d.click(x, y)
    print(f"Clic simulado en ({x}, {y}) - intento {i+1}")
    time.sleep(0.5)