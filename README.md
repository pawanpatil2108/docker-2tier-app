# Docker 2-Tier Application

This project demonstrates a simple 2-tier application using Docker and Docker Compose.

## Architecture
- Web Tier: Python Flask application
- Database Tier: MySQL 5.7
- Docker Compose for orchestration

## Features
- Multi-container setup
- Environment variables for configuration
- Docker volumes for persistent storage
- Healthcheck for database service
- Clean UI using Bootstrap

## How to Run
```bash
docker compose up --build

