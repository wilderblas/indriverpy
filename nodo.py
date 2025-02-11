import uiautomator2 as u2
import xml.etree.ElementTree as ET
import time

def get_ui_hierarchy():
    d = u2.connect()
    hierarchy = d.dump_hierarchy()

    # Guardar el XML en un archivo (opcional)
    with open('ui_dump.xml', 'w', encoding='utf-8') as file:
        file.write(hierarchy)

    try:
        root = ET.fromstring(hierarchy)
        return root
    except ET.ParseError as e:
        print("Error al parsear el XML:", e)
        return None

def extract_node(root):
    # Buscar el nodo específico
    target_node = root.find(".//node[@index='1'][@resource-id='sinet.startup.inDriver:id/page_container']")
    
    if target_node is not None:
        return ET.tostring(target_node, encoding='unicode')
    else:
        return "No se encontró el nodo especificado."

time.sleep(7)  # Espera antes de capturar la UI

ui_root = get_ui_hierarchy()
if ui_root:
    node_xml = extract_node(ui_root)
    print(node_xml)
