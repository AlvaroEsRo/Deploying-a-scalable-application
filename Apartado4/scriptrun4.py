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
    commands = [
        "kubectl apply -f productpage.yaml",
        "kubectl apply -f details.yaml",
        "kubectl apply -f ratings.yaml",
        "kubectl apply -f reviews.yaml",
        "kubectl apply -f reviews-v1.yaml",
        "kubectl apply -f reviews-v2.yaml",
        "kubectl apply -f reviews-v3.yaml",
        "kubectl expose deployment productpage-v1 --type=NodePort --port=9080"
    ]

    for command in commands:
        execute_command(command)

if __name__ == "__main__":
    main()
