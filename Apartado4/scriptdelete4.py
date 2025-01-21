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
        "kubectl delete -f productpage.yaml",
        "kubectl delete -f details.yaml",
        "kubectl delete -f ratings.yaml",
        "kubectl delete -f reviews.yaml",
        "kubectl delete -f reviews-v1.yaml",
        "kubectl delete -f reviews-v2.yaml",
        "kubectl delete -f reviews-v3.yaml",
        "kubectl delete service productpage-v1"
    ]

    for command in commands:
        execute_command(command)

if __name__ == "__main__":
    main()
