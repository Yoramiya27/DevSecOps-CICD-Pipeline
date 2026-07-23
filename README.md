# DevSecOps CI/CD Pipeline with Docker, GitHub Actions, and AWS


INTERN ID: CITS7572
INTERN NAME : JOEL SUJIT
NO OF WEEKS: 4 WEEKS
PROJECT NAME: DEVSECOPOS CI/CD PIPELINE
PROJECT SCOPE: This project is a hands-on implementation of a **DevSecOps workflow** where I built, secured, and deployed a containerized Flask application.
The main goal was to understand how modern software teams automate application delivery while integrating security checks throughout the development process.
During this project, I worked with Git, Docker, GitHub Actions, security scanning tools, and AWS EC2 to create an automated pipeline from code submission to deployment.

---

# Project Architecture

```
Developer
    |
    | Git Push
    ↓
GitHub Repository
    |
    ↓
GitHub Actions Pipeline
    |
    ├── Application Testing
    |
    ├── Gitleaks Secret Scan
    |
    ├── Docker Image Build
    |
    └── Trivy Vulnerability Scan
            |
            ↓
        AWS EC2 Ubuntu Server
            |
            ↓
        Docker Container
            |
            ↓
        Flask Application
```

---

# Technologies Used

### Development

* Python
* Flask

### Version Control

* Git
* GitHub

### Containerization

* Docker

### CI/CD

* GitHub Actions

### Security Tools

* Gitleaks
* Trivy

### Cloud Platform

* AWS EC2
* Ubuntu Server

---

# What I Built

The project started as a simple Flask application and was gradually improved into a complete DevSecOps workflow.

The pipeline automatically:

* Checks out the latest code from GitHub
* Installs project dependencies
* Tests the Flask application
* Scans the repository for exposed secrets
* Builds a Docker image
* Scans the Docker image for vulnerabilities

After passing the security checks, the application is deployed on an AWS EC2 Ubuntu server using Docker.

---

# Project Structure

```
DevSecOps-CICD-Pipeline
│
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker image configuration
├── README.md
│
└── .github
    └── workflows
        └── pipeline.yml    # GitHub Actions workflow
```

---

# CI/CD Pipeline

Every time I push changes to the main branch, GitHub Actions automatically runs the pipeline.

## 1. Testing

The pipeline checks the Python application to ensure there are no syntax issues before continuing.

## 2. Secret Scanning with Gitleaks

Gitleaks checks the repository for accidentally exposed sensitive information such as:

* API keys
* Passwords
* Tokens
* Credentials

## 3. Docker Image Creation

The application is packaged into a Docker image so it can run consistently across different environments.

## 4. Vulnerability Scanning with Trivy

Trivy scans the Docker image and dependencies for known security vulnerabilities.

---

# Docker Deployment

The application was deployed using Docker on an AWS EC2 Ubuntu server.

## Creating the Docker Image

```bash
docker build -t devsecops-app .
```

This creates a Docker image containing:

* Python environment
* Flask application
* Required dependencies

## Running the Container

```bash
docker run -d -p 80:5000 devsecops-app
```

This maps:

```
EC2 Port 80
      |
      ↓
Docker Container Port 5000
      |
      ↓
Flask Application
```

The application can then be accessed using the EC2 public IP address.

---

# AWS Deployment Steps

For deployment, I:

1. Created an AWS EC2 Ubuntu instance
2. Configured SSH access using an EC2 key pair
3. Installed Git and Docker
4. Cloned the project repository
5. Built the Docker image
6. Started the Docker container
7. Hosted the Flask application online

---

# Security Practices Implemented

This project follows basic DevSecOps practices by integrating security into the development workflow instead of treating security as a final step.

Implemented:

* Automated testing
* Secret detection
* Container vulnerability scanning
* Secure deployment practices

---

# Screenshots

In a different folder

---

# Future Improvements

Some improvements I would like to add in the future:

* Automate deployment directly from GitHub Actions to AWS
* Store Docker images using AWS ECR
* Add Infrastructure as Code using Terraform
* Add monitoring and logging
* Explore Kubernetes deployment

---

# What I Learned

Through this project, I gained practical experience with:

* Building and containerizing applications
* Creating CI/CD workflows
* Integrating security tools into pipelines
* Working with Linux servers
* Deploying applications on AWS

---

## Author

Joel Sujit

Computer Science Engineering Student
Cybersecurity Specialization
