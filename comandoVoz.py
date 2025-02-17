import speech_recognition as sr
import uiautomator2 as u2
import time
import os

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="es-ES")
        print(f"Comando reconocido: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return None
    except sr.RequestError:
        print("Error al solicitar resultados; verifica tu conexión a internet")
        return None

def main():
    while True:
      try:
          d = u2.connect()
          if d(textContains="Ofrece tu tarifa").exists():
            command = listen_command()
            if command:
                if "aceptar" in command:
                    print("aceptar")
                elif "primera" in command:
                    print("primera")
                elif "segunda" in command:
                    print("segunda")
                elif "tercera" in command:
                    print("tercera")
                elif "cancelar" in command:
                    print("cancelar")
                    break  # Salir del bucle si se dice "cancela3"
      except Exception as e:
          print(f"Ocurrió un error: {e}")
          break


if __name__ == "__main__":
    main()