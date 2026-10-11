# 🚀 Production-Grade MLOps Iris Classification Pipeline

[![MLOps CI/CD Pipeline](https://github.com/pavithra1436/mlops-iris-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/pavithra1436/mlops-iris-pipeline/actions)
[![Docker Image](https://img.shields.io/docker/v/bpavithra/mlops-iris-pipeline?label=Docker%20Hub)](https://hub.docker.com/r/bpavithra/mlops-iris-pipeline)
[![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/)

An end-to-end automated MLOps pipeline for an Iris Flower Classification model. This repository demonstrates modern MLOps practices including containerization with Docker, automated unit & integration testing, and continuous integration/continuous deployment (CI/CD) using GitHub Actions and Docker Hub.

---

## 📌 Architecture & Features

- **Machine Learning**: Scikit-learn classification model serving predictions for the Iris dataset.
- **REST API**: High-performance FastAPI server delivering predictions and health checks.
- **Testing Suite**: Automated testing with `pytest` and `httpx` to validate model inputs, output schema, and API health.
- **Containerization**: Optimized multi-stage Docker build for isolated, repeatable production deployment.
- **Automated CI/CD**: GitHub Actions workflow automatically runs test suites, builds container images on code push, and pushes tagged images to **Docker Hub**.

---

## 🛠️ Tech Stack

| Domain | Tool / Technology |
| :--- | :--- |
| **Language** | Python 3.9 |
| **Framework** | FastAPI, Uvicorn |
| **Machine Learning** | Scikit-learn (v1.6.1), Joblib, NumPy |
| **Testing** | Pytest, HTTPX |
| **Containerization** | Docker, Docker Compose |
| **CI/CD & Registry** | GitHub Actions, Docker Hub |

---

## 📁 Repository Structure

```text
mlops-prediction-project/
│
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI/CD Pipeline definition
│
├── src/
│   ├── app.py                 # FastAPI application & model inference endpoint
│   ├── model.joblib           # Trained Scikit-learn model artifact
│   ├── test_main.py           # Automated test suite (Pytest)
│   ├── Dockerfile             # Docker container definition
│   └── requirements.txt       # Python project dependencies
│
└── README.md                  # Project documentation