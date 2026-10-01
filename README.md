# Docker Project

A simple Python project using **Pandas** and Docker.

## Project Description

This project demonstrates how to run a Python application inside a Docker container. The application uses the Pandas library to create and analyze student information.

## Project Structure

```text
docker-project/
├── app.py
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

## Python Application

The application creates a student dataset using Pandas and calculates the average age.

Example output:

```text
Student Information
    Name  Age     Major
0  Sabin   23        IT
1  Milan   24        IT
2    Ram   22  Business

Average Age: 23.0
```

## Requirements

* Python 3.12
* Docker
* Pandas 3.0.6

## Dockerfile

The Dockerfile creates a Python environment, installs Pandas, copies the application files, and runs the Python program.

## Build Docker Image

Open a terminal in the project directory and run:

```bash
docker build -t docker-project .
```

## Run Docker Container

```bash
docker run docker-project
```

## Technologies Used

* Python
* Pandas
* Docker
* Git
* GitHub

## Docker Workflow

```text
Python Application
       ↓
   Dockerfile
       ↓
   Docker Image
       ↓
 Docker Container
       ↓
 Application Runs
```

## Learning Outcome

Through this project, I learned the basic concepts of Docker, including Docker images, containers, Dockerfiles, and Docker Compose. I also learned how to package a Python application with its required library and run it inside a Docker container.
