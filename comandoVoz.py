import speech_recognition as sr
import time

time.sleep(8)
recognizer = sr.Recognizer()


try:
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio, language="es-ES")
        print("Dijiste:", text)
except Exception as e:
    print("Ocurrió un error:", e)