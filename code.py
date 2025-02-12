import uiautomator2 as u2
import xml.etree.ElementTree as ET
import time

d=u2.connect()

def buscar_y_clicar_texto(texto):
    d = u2.connect()
    if d(textContains=texto).exists():
        ui_root = get_ui_hierarchy()
        if ui_root:
            node = extract_node(ui_root)
            if node:
                text_values = extract_text_values(node)
                
                # Imprimir los valores en el formato deseado
                """ print(f"driver_common_textview_name = {text_values['sinet.startup.inDriver:id/driver_common_textview_name']}")
                print(f"driver_common_textview_rating = {text_values['sinet.startup.inDriver:id/driver_common_textview_rating']}")
                print(f"driver_common_textview_rating_rides_done = {text_values['sinet.startup.inDriver:id/driver_common_textview_rating_rides_done']}")
                print(f"item_order_textview_posted_time_ago = {text_values['sinet.startup.inDriver:id/item_order_textview_posted_time_ago']}")
                print(f"order_info_textview_from_address = {text_values['sinet.startup.inDriver:id/order_info_textview_from_address']}")
                print(f"order_info_textview_to_addresses = {text_values['sinet.startup.inDriver:id/order_info_textview_to_addresses']}")
                print(f"order_info_textview_price = {text_values['sinet.startup.inDriver:id/order_info_textview_price']}")
                print(f"order_info_textview_distance = {text_values['sinet.startup.inDriver:id/order_info_textview_distance']}") """

                # Imprimir los valores en el formato deseado
                print(f"Nombre = {text_values['sinet.startup.inDriver:id/driver_common_textview_name']}")
                print(f"Rating = {text_values['sinet.startup.inDriver:id/driver_common_textview_rating']}")
                print(f"#viajes = {text_values['sinet.startup.inDriver:id/driver_common_textview_rating_rides_done']}")
                print(f"tiempo de Propuesta = {text_values['sinet.startup.inDriver:id/item_order_textview_posted_time_ago']}")
                print(f"Direccion A = {text_values['sinet.startup.inDriver:id/order_info_textview_from_address']}")
                print(f"Direccion B = {text_values['sinet.startup.inDriver:id/order_info_textview_to_addresses']}")
                print(f"Precio = {text_values['sinet.startup.inDriver:id/order_info_textview_price']}")
                print(f"Distancia = {text_values['sinet.startup.inDriver:id/order_info_textview_distance']}")
            else:
                print("No se encontró el nodo especificado.")
        else:
            print("No se pudo obtener la jerarquía de la UI.")
        d.click(530, 470)
        time.sleep(0.1)

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
    target_node = root.find(".//node[@resource-id='sinet.startup.inDriver:id/item_order_container']")
    
    if target_node is not None:
        return target_node
    else:
        return None

def extract_text_values(node):
    # Diccionario para almacenar los valores de los resource-id
    values = {}

    # Buscar los nodos específicos y extraer sus valores de texto
    resource_ids = [
        "sinet.startup.inDriver:id/driver_common_textview_name",
        "sinet.startup.inDriver:id/driver_common_textview_rating",
        "sinet.startup.inDriver:id/driver_common_textview_rating_rides_done",
        "sinet.startup.inDriver:id/item_order_textview_posted_time_ago",
        "sinet.startup.inDriver:id/order_info_textview_from_address",
        "sinet.startup.inDriver:id/order_info_textview_to_addresses",
        "sinet.startup.inDriver:id/order_info_textview_price",
        "sinet.startup.inDriver:id/order_info_textview_distance"
    ]

    for resource_id in resource_ids:
        element = node.find(f".//node[@resource-id='{resource_id}']")
        if element is not None:
            values[resource_id] = element.get("text", "").strip()
        else:
            values[resource_id] = "No encontrado"

    return values

time.sleep(7)

while True:
    try:
        buscar_y_clicar_texto("metro")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        break
