# README.md
This project demonstrates a production-grade deployment of a full-stack web application on Google Cloud Platform (GCP) using modern infrastructure practices. It is designed for learners and professionals to gain hands-on experience with GCP services and DevOps workflows.

🎯 Project Overview
The goal is to deploy a scalable, secure, and modular web application using the following stack:

Frontend: React-based user interface
Backend: Node.js/Express API server
Infrastructure as Code (IaC): Terraform

Cloud Services:
Compute Engine (for hosting backend/frontend)
Cloud Storage (optional for assets)
VPC networking (with proper subnets/firewalls)
IAM Roles and Service Accounts
Optional: Cloud Run / Cloud Build / Cloud Monitoring


🛠️ Key Features
Modular Terraform scripts to provision VMs, firewall rules, VPC, IAM roles, and network isolation
Automatically deploys multiple virtual machines for frontend and backend
Semantic naming convention and tagging for better visibility and control
Demonstrates network isolation, role-based access control, and SSH access rules
Project is structured for easy CI/CD integration later
