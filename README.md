**CI/CD Pipeline Using GitHub Actions, Docker & Shell Scripting**
Project Overview

This project demonstrates a CI/CD pipeline implemented using GitHub Actions, integrated with Docker containerization and Shell (Bash) scripting.
The pipeline automates build and deployment steps to ensure consistent, repeatable, and reliable application delivery.

This project was created as part of my DevOps hands-on learning and reflects real-world CI/CD practices.

**Tools & Technologies Used**

GitHub Actions – CI/CD automation

Docker – Containerization

Shell Scripting (Bash) – Automation tasks

Git & GitHub – Version control

Linux (Ubuntu) – Execution environment

**CI/CD Workflow**

The pipeline performs the following steps automatically when code is pushed to the repository:

Code Checkout

Pulls the latest source code from the GitHub repository

Build Stage

Builds a Docker image using a Dockerfile

Automation with Shell Scripts

Executes shell scripts for build, deployment, or cleanup tasks

Container Execution

Runs the application inside a Docker container to ensure environment consistency

**Repository Structure**
.
├── .github/workflows/
│   └── pipeline.yml        # GitHub Actions workflow
├── Dockerfile              # Docker image configuration
├── *.sh                    # Shell scripts for automation
└── README.md               # Project documentation

**GitHub Actions Workflow**

Workflow is defined inside .github/workflows/

Automatically triggers on:

push

pull_request

Uses GitHub-hosted runners

Executes Docker and shell commands in sequence

**Docker Implementation**

Uses a Dockerfile to build the application image

Ensures consistent runtime environment

Simplifies deployment and testing across systems

**Shell Scripting**

Shell scripts are used to:

Automate build steps

Execute deployment logic

Reduce manual intervention

Improve reliability and repeatability

**Key Learnings**

Implemented CI/CD using GitHub Actions

Gained hands-on experience with Docker containerization

Automated tasks using Bash scripting

Understood real-world DevOps workflow and pipeline structure

Improved knowledge of Linux-based automation

**Future Enhancements**
Add Docker image push to container registry

Integrate AWS deployment (EC2 / ECS)

Add monitoring and notifications

Improve pipeline security with secrets management

Author

Jayjith R
Linux & DevOps Engineer
GitHub: https://github.com/Jayjith/Pipeline_Setup

LinkedIn: https://www.linkedin.com/in/jayjith
