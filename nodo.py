import subprocess
import xml.etree.ElementTree as ET
import time
import re

def get_ui_hierarchy():
    # Ejecutar el comando adb para obtener el XML de la pantalla
    command = "adb exec-out uiautomator dump /dev/tty"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Verificar si el comando se ejecutó correctamente
    if result.returncode != 0:
        print("Error al obtener la jerarquía de la UI:", result.stderr)
        return None

    # Limpiar la salida eliminando cualquier texto antes y después de <hierarchy>
    match = re.search(r"<hierarchy.*?</hierarchy>", result.stdout, re.DOTALL)
    if match:
        clean_xml = match.group(0)
    else:
        print("Error: No se encontró una estructura XML válida en la salida.")
        return None

    # Parsear el XML
    try:
        root = ET.fromstring(clean_xml)
        return root
    except ET.ParseError as e:
        print("Error al parsear el XML:", e)
        return None

def extract_node(root):
    # Buscar el nodo con resource-id específico
    for node in root.iter("node"):
        if node.get("index") == "1" and node.get("resource-id") == "sinet.startup.inDriver:id/page_container":
            return ET.tostring(node, encoding="unicode")

    return "No se encontró el nodo especificado."

time.sleep(8)

# Obtener la jerarquía de la UI en tiempo real
ui_root = get_ui_hierarchy()

if ui_root is not None:  # 🔧 Corrección aquí
    # Extraer el nodo deseado
    node_xml = extract_node(ui_root)
    print(node_xml)
