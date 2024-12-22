import os
import subprocess

# Asegúrate de que el repositorio exista
if not os.path.exists("practica_creativa2"):
    os.system("git clone https://github.com/CDPS-ETSIT/practica_creativa2.git")

# Cambiar al directorio de reviews
os.chdir("/Users/fugem/Desktop/CDPS/Deploying-a-scalable-application/Apartado3/practica_creativa2/bookinfo/src/reviews")

def build_reviews(version):
    """Compila y construye el servicio Reviews."""
    print(f"Compilando reviews versión {version}...")
    os.chdir("/Users/fugem/Desktop/CDPS/Deploying-a-scalable-application/Apartado3/practica_creativa2/bookinfo/src/reviews")
    subprocess.run([
        "docker", "run", "--rm", "-u", "root", 
        "-v", f"{os.getcwd()}:/home/gradle/project",
        "-w", "/home/gradle/project", 
        "gradle:4.8.1", "gradle", "clean", "build"
    ])
    os.chdir("../../../../")
    subprocess.run([
        "docker", "build", "-t", f"reviews-{version}/08", 
        "/Users/fugem/Desktop/CDPS/Deploying-a-scalable-application/Apartado3/practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg"
    ])

def build_images():
    """Construye todas las imágenes Docker."""
    services = {
        "product-page": "./Dockerfile.product-page",
        "details": "./Dockerfile.details",
        "ratings": "./Dockerfile.ratings"
    }
    for service, dockerfile in services.items():
        print(f"Construyendo imagen para {service}...")
        subprocess.run([
            "docker", "build", "-t", f"{service}/08", "-f", dockerfile, "."
        ])

def start_compose(version):
    """Actualiza docker-compose y levanta los servicios."""
    print("Actualizando versión en docker-compose.yml...")
    with open("docker-compose.yml", "r") as f:
        lines = f.readlines()
    with open("docker-compose.yml", "w") as f:
        for line in lines:
            if "SERVICE_VERSION" in line:
                f.write(f"      - SERVICE_VERSION={version}\n")
            else:
                f.write(line)
    print("Levantando servicios con docker-compose...")
    subprocess.run(["docker-compose", "up", "-d"])

if __name__ == "__main__":
    # Cambia entre las versiones según sea necesario
    reviews_version = "v1"  # Cambiar a v2 o v3 según la prueba
    build_reviews(reviews_version)
    build_images()
    start_compose(reviews_version)
