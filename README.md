# Azure-Powered Web Application Deployment

## Overview

This project demonstrates the deployment of a web application to **Azure App Services** using **Docker**, **Azure Container Registry (ACR)**, and **GitHub Actions**. The main objectives of this project are to:
- Create a deployable Docker image.
- Automate deployment via GitHub Actions.
- Utilize Azure services for secure and efficient application hosting.

This application is designed as part of an academic project and adheres to industry best practices for CI/CD and cloud deployment.

---

### Dockerfile
- Builds a Docker image of the web application.
- Exposes ports for SSH and web server communication.
- Includes an initialization script for setting up SSH and starting the web server.

### Azure Container Registry (ACR)
- Stores the Docker image securely.
- Provides seamless integration with Azure App Services.

### GitHub Actions Workflow
- Automates the process of:
  - Authenticating with Azure using `AZURE_CREDENTIALS`.
  - Building and pushing the Docker image to ACR.
  - Triggering deployment to Azure App Service.

### Deployment
- Utilizes **User Assigned Identity** for secure communication between Azure services.
- Ensures end-to-end automation of the deployment pipeline.

---

## Features

- **Continuous Integration/Continuous Deployment (CI/CD)**:
  - Streamlined automation using GitHub Actions.

- **Secure and Scalable Deployment**:
  - Leveraging Azure's secure infrastructure.
  - Scalable hosting via Azure App Services.

- **Dockerized Application**:
  - Encapsulation of application dependencies and configurations for portability.

---

## Assumptions and Configurations

### Azure Setup
- An Azure account is required with permissions for:
  - Creating and managing Azure App Services.
  - Setting up ACR with appropriate credentials.

### Git Workflow
- A structured branching strategy is followed as assigned during the midterm project.

### Environment Variables
- The following environment variables are required in GitHub Actions:
  - `AZURE_CREDENTIALS`
  - `REGISTRY_USERNAME`
  - `REGISTRY_PASSWORD`

### Dockerfile
- Exposes necessary ports for SSH and web access.
- Includes commands to set up the web server.

---

## Data Flow

1. **Local Development**:
   - Develop and test the application locally using Docker.

2. **Push to GitHub**:
   - Push changes to the relevant branch to trigger GitHub Actions.

3. **CI/CD Pipeline**:
   - GitHub Actions builds the Docker image and pushes it to ACR.
   - Deploys the application to Azure App Services.

4. **Deployment Verification**:
   - Verify the application is running correctly on the Azure App Service.

---

## Data Model (Example)

While the project requirements do not specify a particular application type, a sample data model for a web application might include:

| **Field**           | **Type** | **Description**                          |
|----------------------|----------|------------------------------------------|
| `id`                | INTEGER  | Primary key, auto-incremented.           |
| `title`             | TEXT     | Title of the content.                    |
| `description`       | TEXT     | Brief description of the content.        |
| `image_url`         | TEXT     | Path to the image associated with the content. |
| `created_at`        | DATETIME | Timestamp of when the content was added. |

---

## How to Use

### Prerequisites
- Docker installed locally.
- Azure CLI installed and configured.
- A GitHub repository with GitHub Actions enabled.

### Steps to Deploy
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>

---

## Live Demo

You can access the live demo of this application at the following link:

- [Azure Deployed Application](https://se4453final.azurewebsites.net)

---

