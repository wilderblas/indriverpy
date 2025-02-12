import uiautomator2 as u2
import xml.etree.ElementTree as ET
import time
import googlemaps
#import math
import re
import os

nombre=""
rating=0.0
nviajes=0
tPropuestaSec=0
precio=0.0
distanciaA=0
distanciaB=0
propuestaSol=0.0
precioAceptado=0

API_KEY = "AIzaSyCC4wcwBPCcqJvYyk5RiRPj_2J1kGzNrrs"
# Inicializar el cliente de Google Maps
gmaps = googlemaps.Client(key=API_KEY)

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
                nombre=f"{text_values['sinet.startup.inDriver:id/driver_common_textview_name']}"
                print(f"Rating = {text_values['sinet.startup.inDriver:id/driver_common_textview_rating']}")
                rating=float(f"{text_values['sinet.startup.inDriver:id/driver_common_textview_rating']}")
                print(f"#viajes = {text_values['sinet.startup.inDriver:id/driver_common_textview_rating_rides_done']}")
                nviajes=int((f"{text_values['sinet.startup.inDriver:id/driver_common_textview_rating_rides_done']}").strip("()"))
                print(f"tiempo de Propuesta = {text_values['sinet.startup.inDriver:id/item_order_textview_posted_time_ago']}")
                tPropuestaSec=convertir_a_segundos(f"{text_values['sinet.startup.inDriver:id/item_order_textview_posted_time_ago']}")
                # Direcciones en Trujillo, La Libertad, Perú
                origen = f"{text_values['sinet.startup.inDriver:id/order_info_textview_from_address']}, Trujillo, La Libertad, Perú"
                destino = f"{text_values['sinet.startup.inDriver:id/order_info_textview_to_addresses']}, Trujillo, La Libertad, Perú"
                # Obtener la distancia con la API Distance Matrix
                resultado = gmaps.distance_matrix(origen, destino, mode="driving")
                #print(f"Direccion A = {text_values['sinet.startup.inDriver:id/order_info_textview_from_address']}")
                #print(f"Direccion B = {text_values['sinet.startup.inDriver:id/order_info_textview_to_addresses']}")
                if resultado["rows"][0]["elements"][0]["status"] == "OK":
                    distancia_metros = resultado["rows"][0]["elements"][0]["distance"]["value"]
                    distancia_km = distancia_metros / 1000  # Convertir a kilómetros

                    duracion_segundos = resultado["rows"][0]["elements"][0]["duration"]["value"]
                    duracion_minutos = duracion_segundos / 60  # Convertir a minutos
                    
                    print(f"La distancia entre {origen} y {destino} es {distancia_km:.2f} km")
                    print(f"El tiempo estimado de viaje en auto es de {duracion_minutos:.2f} minutos")
                else:
                    print("No se pudo calcular la distancia o el tiempo de viaje.")
                print(f"Precio = {text_values['sinet.startup.inDriver:id/order_info_textview_price']}")
                precio=float((f"{text_values['sinet.startup.inDriver:id/order_info_textview_price']}").replace("S/ ",""))
                print(f"Distancia = {text_values['sinet.startup.inDriver:id/order_info_textview_distance']}")
                distanciaA=extraer_metros(f"{text_values['sinet.startup.inDriver:id/order_info_textview_distance']}")
            else:
                print("No se encontró el nodo especificado.")
        else:
            print("No se pudo obtener la jerarquía de la UI.")
        d.click(530, 470)
        time.sleep(0.1)
        print("Variables")
        print("nombre="+nombre)
        print("rating="+str(rating))
        print("nviajes="+str(nviajes))
        print("tPropuestaSec="+str(tPropuestaSec))
        print("precio="+str(precio))
        print("distanciaA="+str(distanciaA))
        print("distanciaB="+str(distancia_metros))
        time.sleep(0.3)
        while True:
            try:
                d = u2.connect()
                if d(textContains="Ofrece tu tarifa").exists():
                    if distancia_metros<1000:
                        print("Aceptar la propuesta la que sea")
                    else:
                        root = get_ui_hierarchy()
                        if root is not None:
                            propuestaSol = float(extract_price(root).replace("S/ ",""))
                            print("Precio encontrado: "+str(propuestaSol))
                            if distancia_metros<6500:
                                if duracion_minutos < 7 and duracion_minutos > 5.20:
                                    precioAceptado=6
                                else:
                                    precioAceptado=round(duracion_minutos*0.66)
                                if propuestaSol>=precioAceptado:
                                    #click boton aceptado
                                    print("Se ACEPTA la propuesta del CIENTE")
                                    time.sleep(10)
                                else:
                                    d.click(976,2049)
                                    time.sleep(0.2)
                                    d.click(976,2049)
                                    time.sleep(0.1)
                                    enviar_texto_por_adb(str(precioAceptado))
                                    print("Se presiona enter")
                                    time.sleep(10)
                            else:
                                if distancia_metros<8000:
                                    precioAceptado=round(duracion_minutos*0.64)
                                    if propuestaSol>=precioAceptado:
                                        #clicl boton Aceptado
                                        print("Se ACEPTA la propuesta del CIENTE")
                                        time.sleep(10)
                                    else:
                                        d.click(976,2049)
                                        time.sleep(0.2)
                                        d.click(976,2049)
                                        time.sleep(0.1)
                                        enviar_texto_por_adb(str(precioAceptado))
                                        print("Se presiona enter")
                                        time.sleep(10)
                                else:
                                    #back
                                    print("Saldre del bucle porque la carrera es mayor a 8 Km")
                                    break
                            #precio=float((f"{text_values['sinet.startup.inDriver:id/order_info_textview_price']}").replace("S/ ",""))
                        else:
                            print("No se pudo obtener la jerarquía de la UI.")
            except Exception as e:
                print(f"Ocurrió un error: {e}")
                break

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

def extract_price(root):
    # Buscar el nodo específico que contiene el precio
    price_node = root.find(".//node[@resource-id='sinet.startup.inDriver:id/info_textview_price']")
    
    if price_node is not None:
        return price_node.get("text", "").strip()
    else:
        return "No encontrado"

def convertir_a_segundos(texto):
    """Convierte un string de tiempo en segundos."""
    if texto == "Justo ahora":
        return 0  # Si es "Justo ahora", retorna 0

    match = re.match(r"(\d+)\s*(\w+)\.", texto)  # Extraer número y unidad
    if match:
        valor, unidad = int(match.group(1)), match.group(2)
        
        if "seg" in unidad:
            return valor  # Si es segundos, retorna tal cual
        elif "min" in unidad:
            return valor * 60  # Si es minutos, multiplica por 60

    return None

def extraer_metros(texto):
    """Elimina '~', convierte 'km' a metros y devuelve un entero."""
    texto = texto.replace("~", "").replace(",", ".")  # Elimina '~' y cambia ',' por '.'
    
    if "km" in texto:
        return int(float(texto.replace(" km", "")) * 1000)  # Convierte km a metros
    elif "metro" in texto:
        return int(float(texto.replace(" metro", "")))  # Mantiene metros
    
    return None  # Si no contiene 'metro' o 'km', retorna None

def enviar_texto_por_adb(texto):
    comando = f"adb shell input text \"{texto}\""
    os.system(comando)

time.sleep(7)

while True:
    try:
        buscar_y_clicar_texto("metro")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        break
