import uiautomator2 as u2
import time
#import subprocess

carreraTomada = False
# Conectar con el dispositivo (asegúrate de que tu dispositivo esté conectado y en modo depuración)

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
        print("El texto fue encontrado en la pantalla.")
    else:
        print("El texto no fue encontrado.")

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
        buscar_y_clicar_texto("metro")
        time.sleep(2)
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        break

""" time.sleep(7)
d = u2.connect()
hierarchy = d.dump_hierarchy()

# Guardar en un archivo de texto
with open('hierarchy.xml', 'w', encoding='utf-8') as file:
    file.write(hierarchy) """