import subprocess

def execute_command(command):
    try:
        print(f"Executing: {command}")
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error: {e.stderr}")
        exit(1)

def get_active_reviews_version():
    try:
        # Obtener despliegues activos que contienen "reviews"
        result = subprocess.run(
            "kubectl get deployments | grep reviews | awk '{print $1}'",
            shell=True,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        deployments = result.stdout.strip().split("\n")
        # Filtrar para detectar versiones
        for deployment in deployments:
            if deployment.startswith("reviews-"):
                return deployment  # Retorna el nombre completo, como "reviews-v1"
        print("No active reviews deployment found.")
        exit(1)
    except subprocess.CalledProcessError as e:
        print("Error detecting active reviews deployment.")
        print(f"Error: {e.stderr}")
        exit(1)

def main():
    # Detectar versión activa de reviews
    active_reviews = get_active_reviews_version()
    print(f"Detected active reviews deployment: {active_reviews}")

    # Comandos generales para eliminar
    commands = [
        "kubectl delete -f productpage.yaml",
        "kubectl delete -f details.yaml",
        "kubectl delete -f ratings.yaml",
        "kubectl delete -f reviews.yaml",
        f"kubectl delete -f {active_reviews}.yaml",  # Eliminar la versión detectada
        "kubectl delete service productpage-v1"
    ]

    for command in commands:
        execute_command(command)

if __name__ == "__main__":
    main()
