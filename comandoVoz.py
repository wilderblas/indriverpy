import subprocess
import time

time.sleep(8)

print("Esperando entrada del teclado... Presiona 'Q' para salir.")

# Ejecuta el comando `getevent -l` para capturar eventos del teclado
process = subprocess.Popen(["adb", "shell", "getevent -l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

try:
    for line in process.stdout:
        if "KEY_W" in line:
            print("Aceptar")
        elif "KEY_A" in line:
            print("Opcion1")
        elif "KEY_S" in line:
            print("Opcion2")
        elif "KEY_D" in line:
            print("Opcion3")
        elif "KEY_X" in line:
            print("Cerrar")
        elif "KEY_Q" in line:
            print("Saliendo...")
            process.terminate()
            exit(0)
except KeyboardInterrupt:
    print("Saliendo...")
    process.terminate()