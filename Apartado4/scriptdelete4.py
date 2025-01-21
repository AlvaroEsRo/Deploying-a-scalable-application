import subprocess

def execute_command(command):
    try:
        print(f"Executing: {command}")
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error: {e.stderr}")

def get_active_resources(resource_type):
    """
    Obtiene los recursos activos de Kubernetes según el tipo especificado (deployments o services).
    """
    try:
        # Obtener la lista de recursos activos
        command = f"kubectl get {resource_type} -o name"
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        resources = result.stdout.strip().split("\n")
        return [resource.split("/")[1] for resource in resources if resource]  # Extraer solo el nombre del recurso
    except subprocess.CalledProcessError as e:
        print(f"Error getting active {resource_type}: {e.stderr}")
        return []

def main():
    # Obtener deployments y services activos
    active_deployments = get_active_resources("deployments")
    active_services = get_active_resources("services")

    print("Active Deployments:")
    for deployment in active_deployments:
        print(f"  - {deployment}")
    
    print("Active Services:")
    for service in active_services:
        print(f"  - {service}")

    # Eliminar deployments activos
    for deployment in active_deployments:
        command = f"kubectl delete deployment {deployment}"
        execute_command(command)

    # Eliminar servicios activos
    for service in active_services:
        command = f"kubectl delete service {service}"
        execute_command(command)

if __name__ == "__main__":
    main()
