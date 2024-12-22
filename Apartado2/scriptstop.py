import subprocess

# Configuración
CONTAINER_NAME = "product-page-08"  # Nombre del contenedor

def stop_container():
    """Detiene el contenedor Docker."""
    print(f"Deteniendo el contenedor {CONTAINER_NAME}...")
    result = subprocess.run(["docker", "stop", CONTAINER_NAME], capture_output=True, text=True)
    if result.returncode == 0:
        print("Contenedor detenido exitosamente.")
    else:
        print(f"Error al detener el contenedor:\n{result.stderr}")

def remove_container():
    """Elimina el contenedor Docker."""
    print(f"Eliminando el contenedor {CONTAINER_NAME}...")
    result = subprocess.run(["docker", "rm", CONTAINER_NAME], capture_output=True, text=True)
    if result.returncode == 0:
        print("Contenedor eliminado exitosamente.")
    else:
        print(f"Error al eliminar el contenedor:\n{result.stderr}")

def clean():
    """Elimina el contenedor Docker."""
    print(f"limpiando el sistema {CONTAINER_NAME}...")
    result = subprocess.run(["docker", "system", "prune", "-f"], capture_output=True, text=True)
    if result.returncode == 0:
        print("Contenedor limpiado exitosamente.")
    else:
        print(f"Error al limpiar el contenedor:\n{result.stderr}")

if __name__ == "__main__":
    stop_container()
    remove_container()
    clean()
