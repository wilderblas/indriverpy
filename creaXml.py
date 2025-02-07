import uiautomator2 as u2
import time

time.sleep(7)

d = u2.connect()
hierarchy = d.dump_hierarchy()

# Guardar en un archivo de texto
with open('SolicitudDViaje1.xml', 'w', encoding='utf-8') as file:
    file.write(hierarchy)