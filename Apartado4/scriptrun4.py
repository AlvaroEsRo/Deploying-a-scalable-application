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

def main():
    # Solicitar la versión de reviews
    print("Available versions: v1, v2, v3")
    version = input("Enter the version of reviews to deploy: ").strip()

    # Validar la entrada
    if version not in ["v1", "v2", "v3"]:
        print("Invalid version. Please choose v1, v2, or v3.")
        exit(1)

    # Comandos generales
    commands = [
        "kubectl apply -f productpage.yaml",
        "kubectl apply -f details.yaml",
        "kubectl apply -f ratings.yaml",
        "kubectl apply -f reviews.yaml",
        f"kubectl apply -f reviews-{version}.yaml",
        "kubectl expose deployment productpage-v1 --type=NodePort --port=9080"
    ]

    for command in commands:
        execute_command(command)

if __name__ == "__main__":
    main()
