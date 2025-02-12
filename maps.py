import googlemaps

# Reemplaza con tu clave de API de Google Maps
API_KEY = "AIzaSyCC4wcwBPCcqJvYyk5RiRPj_2J1kGzNrrs"

# Inicializar el cliente de Google Maps
gmaps = googlemaps.Client(key=API_KEY)

# Direcciones en Trujillo, La Libertad, Perú
origen = "El Tigre 282 (Trujillo), Trujillo, La Libertad, Perú"
destino = "Larco Gym (Calle los Ficus, Victor Larco Herrera), Trujillo, La Libertad, Perú"

# Obtener la distancia con la API Distance Matrix
resultado = gmaps.distance_matrix(origen, destino, mode="driving")

# Extraer la distancia en kilómetros
if resultado["rows"][0]["elements"][0]["status"] == "OK":
    distancia_metros = resultado["rows"][0]["elements"][0]["distance"]["value"]
    distancia_km = distancia_metros / 1000  # Convertir a kilómetros
    print(f"La distancia entre {origen} y {destino} es {distancia_km} km")
else:
    print("No se pudo calcular la distancia.")