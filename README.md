# Deploying-a-scalable-application

This project contains several sections demonstrating how to deploy and manage scalable applications using Docker, Docker Compose, and Kubernetes.

## Section 1: Initial Configuration Script

The script [ScriptPaso1.py](Apartado1/ScriptPaso1.py) performs the following tasks:
- Clones a GitHub repository.
- Updates system packages and installs Python 3 and pip.
- Modifies the `requirements.txt` file to avoid incompatibilities.
- Installs project dependencies.
- Modifies HTML files to include the group number.
- Creates a firewall rule in Google Cloud to allow traffic on the specified port.
- Launches the application on the specified port.

## Section 2: Docker

### Dockerfile

The [Dockerfile](Apartado2/Dockerfile) defines a Docker image for the `product-page` application. It performs the following tasks:
- Uses a lightweight Python base image.
- Installs system dependencies and clones the repository.
- Modifies the `requirements.txt` file.
- Copies the `update_title.py` script.
- Installs Python dependencies.
- Exposes port 9080 and defines the default command to run the application.

### Scripts

- [scriptrun2.py](Apartado2/scriptrun2.py): Builds and runs the Docker container.
- [scriptstop2.py](Apartado2/scriptstop2.py): Stops and removes the Docker container, and cleans the system.
- [update_title.py](Apartado2/update_title.py): Modifies HTML files to include the group number.

### Useful Commands

To view the container logs:

``
docker logs product-page-08
``

## Section 3: Docker Compose

The [docker-compose.yml](Apartado3/docker-compose.yml) file defines the services for the application using Docker Compose. It includes the following services:
- `g08-details`
- `g08-ratings`
- `g08-reviews`
- `g08-productpage`

### Dockerfiles

- [Dockerfile.details](Apartado3/Dockerfile.details): Defines the Docker image for the `details` service.
- [Dockerfile.ratings](Apartado3/Dockerfile.ratings): Defines the Docker image for the `ratings` service.
- [Dockerfile.product-page](Apartado3/Dockerfile.product-page): Defines the Docker image for the `product-page` service.

### Script

- [microservices.py](Apartado3/microservices.py): Configures the versions of the `reviews` services, creates firewall rules, compiles, and deploys the services using Docker Compose.

## Section 4: Kubernetes

### Configuration Files

- [details.yaml](Apartado4/details.yaml): Defines the service and deployment for `details`.
- [productpage.yaml](Apartado4/productpage.yaml): Defines the service and deployment for `productpage`.
- [ratings.yaml](Apartado4/ratings.yaml): Defines the service and deployment for `ratings`.
- [reviews.yaml](Apartado4/reviews.yaml): Defines the service for `reviews`.
- [reviews-v1.yaml](Apartado4/reviews-v1.yaml): Defines the deployment for `reviews` version 1.
- [reviews-v2.yaml](Apartado4/reviews-v2.yaml): Defines the deployment for `reviews` version 2.
- [reviews-v3.yaml](Apartado4/reviews-v3.yaml): Defines the deployment for `reviews` version 3.

### Dockerfiles

- [Dockerfile.details](Apartado4/Dockerfile.details): Defines the Docker image for the `details` service.
- [Dockerfile.ratings](Apartado4/Dockerfile.ratings): Defines the Docker image for the `ratings` service.

## Deployment Instructions

### Docker

To build and run the Docker image:

``
python3 scriptrun2.py
``

To stop and remove the Docker container:

``
python3 scriptstop2.py
``

### Docker Compose

To deploy the services using Docker Compose:

``
python3 microservices.py
``

### Kubernetes

To deploy the services in Kubernetes:

``
kubectl apply -f .yaml
``

``
kubectl expose deployment productpage-v1 --type=NodePort --port=9080
``