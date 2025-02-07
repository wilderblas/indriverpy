import uiautomator2 as u2
import time
import os
import threading

#import subprocess

carreraTomada = False
# Conectar con el dispositivo (asegúrate de que tu dispositivo esté conectado y en modo depuración)

d = u2.connect()  # Conecta al primer dispositivo disponible

""" def tarea1(d):
    d.click(530,670)

def tarea2():
    os.system("mpv sonido.mp3")

hilo1 = threading.Thread(target=tarea1)
hilo2 = threading.Thread(target=tarea2) """

# Función para hacer clic
def hacer_clic():
    d.click(530, 470)
    print("Clic realizado.")

# Función para reproducir el sonido
def reproducir_sonido():
    os.system("mpv sonido.mp3")
    print("Sonido reproducido.")

def buscar_y_clicar_texto(texto):
    # Conectar al dispositivo
    d = u2.connect()  # Conecta al primer dispositivo disponible
    
    # Buscar el texto en la pantalla
    #elemento = d(text=texto)
    
    """ if elemento.exists:
        # Si el texto existe, hacer clic en él
        #elemento.click(500,500)
        print(f"Se encontró el texto")
    else:
        print(f"No se encontró el texto")
        #elemento.click() """
    if d(textContains=texto).exists():
        # Crear hilos para ambas acciones
        sonido_thread = threading.Thread(target=reproducir_sonido)
        clic_thread = threading.Thread(target=hacer_clic)
        
        # Iniciar ambos hilos
        sonido_thread.start()
        clic_thread.start()
        
        # Esperar a que ambos hilos terminen
        sonido_thread.join()
        clic_thread.join()
        time.sleep(0.2)
    else:
        d.swipe(500, 350, 500, 1100, duration=0.4)

        #print("El texto fue encontrado en la pantalla.")
    #else:
        #print("El texto no fue encontrado.")

#d = u2.connect()

# Verifica que la conexión funciona
#print(d.info)

# Coordenadas del clic
""" x, y = 500, 600
time.sleep(5) """

# Simula clics
""" for i in range(4):
    d.click(x, y)
    print(f"Clic simulado en ({x}, {y}) - intento {i+1}")
    time.sleep(0.5) """





time.sleep(7)

while not carreraTomada:
    try:
        if d(text="Solicitudes de viaje").exists():
            print("Solicitudes de Viaje")
            buscar_y_clicar_texto("metro")
            time.sleep(0.4)
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        break




""" time.sleep(7)
d = u2.connect()
hierarchy = d.dump_hierarchy()

# Guardar en un archivo de texto
with open('SolicitudDViaje.xml', 'w', encoding='utf-8') as file:
    file.write(hierarchy) """
