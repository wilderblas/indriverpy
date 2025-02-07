from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def calcular_distancia(direccion1, direccion2):
    geolocator = Nominatim(user_agent="geoapiExercises")
    
    # Obtener coordenadas de las direcciones
    ubicacion1 = geolocator.geocode(direccion1)
    ubicacion2 = geolocator.geocode(direccion2)

    if ubicacion1 and ubicacion2:
        coords1 = (ubicacion1.latitude, ubicacion1.longitude)
        coords2 = (ubicacion2.latitude, ubicacion2.longitude)
        
        distancia = geodesic(coords1, coords2).km
        return distancia
    else:
        return "No se pudo encontrar una de las direcciones."

# Ejemplo de uso
direccion_origen = "Av. Hermanos Uceda Meza 638 (Urb las Quintanas Etapa 4)"
direccion_destino = "Complejo deportivo CEP Nuestra Señora del Perpetuo Socorro"

distancia_km = calcular_distancia(direccion_origen, direccion_destino)
print(f"La distancia es aproximadamente {distancia_km:.2f} km")
