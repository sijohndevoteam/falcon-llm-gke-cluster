# Deploy Open Source LLM's to Google Cloud Infra

This ReadMe.md file provides instructions on how to deploy open-source language models like Falcon-7B or Dolly by Databricks models in a containerized cloud environment on Google Cloud Infrastructure. The deployment will make these models accessible through an API endpoint, and we'll create a Gradio app to interact with the models.

## Toolbox Essentials: Gathering Components

Running open-source models with substantial computational demands like Falcon-7B requires GPU support. To solve this challenge, we'll leverage GPUs in the cloud. For containerization and GPU support, we'll use an open-source tool called Truss. Truss allows developers to containerize models easily by automatically generating a Dockerfile and managing Python dependencies.

## The Blueprint

1. **Set up Falcon 7B using Truss**: Create a new Python project with Python version ≥ 3.8, and install Truss. Configure Truss using `truss init falcon_7b_truss` to create necessary files.

2. **Containerize the model and run it using Docker**: In the `main.py` file, work with Truss to bundle everything together. Build the Docker image using the command: `docker build falcon_7b_truss -t falcon-7b-model:latest`. Tag and push the image to a Container Registry like Google Artifact Registry.

3. **Create a GPU-equipped Kubernetes cluster in Google Kubernetes Engine (GKE)**: Create a GKE cluster with GPU support, and connect it to the Container Registry.

4. **Deploy the model to GKE & expose the model running in the cluster using an Internal LoadBalancer (ILB)**: Deploy the containerized model on GKE using a Kubernetes Deployment and Service with GPU support. Expose the service through an ILB to make it accessible within the VPC.

5. **Consume the model using a Gradio app running in Google Cloud Run instance**: Create a Gradio app that interacts with the deployed model on GKE. Host the Gradio app on Cloud Run and use a Serverless VPC Connector to access the model running in the GKE cluster.

## Usage Instructions

1. Clone the repository.

2. Set up Python Virtual Env (recommended): `python3 -m venv env_name` and `source env_name/bin/activate`.

3. Install required dependencies: `pip3 install truss`.

4. Create a new project and initialize Truss: `truss init falcon_7b_truss`.

5. Update `model.py` with the provided code for the Falcon-7B model.

6. Containerize the model using Truss: `python3 main.py`.

7. Build the Docker image and push it to a Container Registry like Google Artifact Registry or Docker Hub.

8. Create a GPU-enabled GKE cluster using the provided configurations.

9. Deploy the model to the GKE cluster using Kubernetes.

10. Create a Gradio app (`app.py`) that interacts with the model API running on the GKE cluster.

11. Build the Docker image for the Gradio app and deploy it to Google Cloud Run.

12. Access the Gradio app via the Cloud Run endpoint.

Note: For detailed step-by-step instructions, refer to the original article.

## Port Forwarding

kubectl port-forward svc/truss-falcon-7b-service-cluster-ip 8080

You should get Output
 Forwarding from 127.0.0.1:8080 -> 8080
 Forwarding from [::1]:8080 -> 8080