import googlemaps

def distancia_google_maps(direccion1, direccion2, api_key):
    gmaps = googlemaps.Client(key=api_key)
    
    resultado = gmaps.distance_matrix(direccion1, direccion2, mode="driving")
    distancia = resultado["rows"][0]["elements"][0]["distance"]["text"]
    
    return distancia

# Clave de API de Google Maps (debes generar una en Google Cloud)
API_KEY = "AIzaSyCC4wcwBPCcqJvYyk5RiRPj_2J1kGzNrrs"

direccion_origen = "Av. Hermanos Uceda Meza 638 (Urb las Quintanas Etapa 4)"
direccion_destino = "Complejo deportivo CEP Nuestra Señora del Perpetuo Socorro"

distancia_km = distancia_google_maps(direccion_origen, direccion_destino, API_KEY)
print(f"La distancia por carretera es aproximadamente {distancia_km}")

# Ejemplo de uso
#direccion_origen = "Av. Hermanos Uceda Meza 638 (Urb las Quintanas Etapa 4)"
#direccion_destino = "Complejo deportivo CEP Nuestra Señora del Perpetuo Socorro"

