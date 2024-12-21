import subprocess

# Configuración de la aplicación
REPO_URL = "https://github.com/CDPS-ETSIT/practica_creativa2.git"
GROUP_NAME = "07"
APP_PORT = 9080  # Puerto en el que se ejecutará la aplicación
VENV_PATH = "venv"  # Ruta para el entorno virtual

# Comandos para configurar e iniciar la aplicación
commands = [
    "sudo apt-get update && sudo apt-get upgrade -y",
    "sudo apt-get install -y python3 python3-pip python3-venv git",
    f"git clone {REPO_URL}",
    # Modificar el archivo requirements.txt antes de instalar dependencias
    '''python3 -c "
with open('practica_creativa2/bookinfo/src/productpage/requirements.txt', 'r') as file:
    requirements = file.read()
requirements = requirements.replace('urllib3==1.26.5', 'urllib3<1.25')
with open('practica_creativa2/bookinfo/src/productpage/requirements.txt', 'w') as file:
    file.write(requirements)
"''',
    f"cd practica_creativa2/bookinfo/src/productpage && python3 -m venv {VENV_PATH}",
    f"source practica_creativa2/bookinfo/src/productpage/{VENV_PATH}/bin/activate && pip install -r practica_creativa2/bookinfo/src/productpage/requirements.txt",
    f"source practica_creativa2/bookinfo/src/productpage/{VENV_PATH}/bin/activate && export GRUP_NUM={GROUP_NAME} && nohup python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py {APP_PORT} > app.log 2>&1 &",
]

def run_commands(commands):
    """Ejecuta una lista de comandos en la VM local."""
    for command in commands:
        print(f"Ejecutando: {command}")
        try:
            subprocess.run(command, shell=True, check=True, executable="/bin/bash")
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el comando: {e}")
            break

if __name__ == "__main__":
    run_commands(commands)
    print(f"Despliegue completado. Accede a la aplicación en el puerto {APP_PORT}.")
