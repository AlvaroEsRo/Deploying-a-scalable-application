import os
import subprocess

# Configuración
DOCKERFILE_PATH = "./"  # Ruta donde se encuentra el Dockerfile
IMAGE_NAME = "product-page/08"  # Nombre de la imagen Docker
CONTAINER_NAME = "product-page-08"  # Nombre del contenedor
GROUP_NUM = "08"  # Número del grupo
PORT = "9080"  # Puerto para la aplicación

def build_image():
    """Construye la imagen Docker."""
    print(f"Construyendo la imagen {IMAGE_NAME}...")
    result = subprocess.run(["docker", "build", "-t", IMAGE_NAME, DOCKERFILE_PATH], capture_output=True, text=True)
    if result.returncode == 0:
        print("Imagen construida exitosamente.")
    else:
        print(f"Error al construir la imagen:\n{result.stderr}")

def run_container():
    """Ejecuta el contenedor Docker."""
    print(f"Iniciando el contenedor {CONTAINER_NAME}...")
    result = subprocess.run([
        "docker", "run", "--name", CONTAINER_NAME,
        "-p", f"{PORT}:{PORT}",
        "-e", f"GROUP_NUM={GROUP_NUM}",
        "-d", IMAGE_NAME
    ], capture_output=True, text=True)
    if result.returncode == 0:
        print("Contenedor iniciado exitosamente.")
    else:
        print(f"Error al iniciar el contenedor:\n{result.stderr}")

if __name__ == "__main__":
    build_image()
    run_container()
