import sys
import os

def cambiarVariablesEntornoCompose(version):
    with open("docker-compose.yml", "r") as f:
        lines = f.readlines()

    updated_lines = []
    for line in lines:
        if "SERVICE_VERSION" in line:
            line = f"      - SERVICE_VERSION={version}\n"
        if "ENABLE_RATINGS" in line:
            line = f"      - ENABLE_RATINGS={'true' if version in ['v2', 'v3'] else 'false'}\n"
        if "STAR_COLOR" in line:
            line = f"      - STAR_COLOR={'red' if version == 'v3' else 'black'}\n"
        updated_lines.append(line)

    with open("docker-compose.yml", "w") as f:
        f.writelines(updated_lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <version>")
        sys.exit(1)

    version = sys.argv[1]
    cambiarVariablesEntornoCompose(version)

    # Compilar el servicio Reviews
    os.chdir('practica_creativa2/bookinfo/src/reviews')
    os.system('docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build')
    os.chdir('../../../../')

    # Crear imágenes Docker
    os.system("docker buildx build --platform linux/amd64 -t g08/reviews practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg")
    os.system("docker build -t g08/productpage -f Dockerfile.product-page .")
    os.system("docker build -t g08/details -f Dockerfile.details .")
    os.system("docker build -t g08/ratings -f Dockerfile.ratings .")

    # Desplegar con Docker Compose
    os.system("docker-compose up -d")

print("Despliegue completado.")
