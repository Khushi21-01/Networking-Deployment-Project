# Automated Container Deployment and Administration in the Cloud
## Automated Flask App Deployment on Azure using Terraform, Ansible, Docker & GitHub Actions

This project demonstrates end-to-end automation of cloud infrastructure provisioning and Docker-based application deployment using modern DevOps tools. A Flask web application is deployed to an Azure VM, with all configuration and deployment steps automated using:

-  Terraform for infrastructure provisioning  
-  Ansible for server configuration and Docker deployment  
-  Docker to containerize the Flask app  
-  GitHub Actions for CI/CD automation

---
## Project Structure
```
azure-auto-deploy/
├── terraform/                # Infrastructure setup using Terraform
│   ├── main.tf
│   └── outputs.tf
├── sample-app/               # Flask app with Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── ansible/                  # Server with Ansible
│   ├── inventory.ini
│   └── docker.yml
├── .github/workflows/        # CI/CD configuration
│   └── deploy.yml
├── README.md
```
---

##  Tools Used

- [Terraform](https://www.terraform.io/)
- [Ansible](https://www.ansible.com/)
- [Docker](https://www.docker.com/)
- [GitHub Actions](https://github.com/features/actions)
- [Azure](https://portal.azure.com/)

---

##  What It Does

1. Provisions an **Ubuntu VM on Azure** using Terraform
2. Uses **Ansible** to:
   - Install Docker
   - Copy and build the Flask app into a container
   - Run the container on port 80
3. Uses **GitHub Actions** to:
   - Trigger the pipeline on code push
   - SSH into Azure VM
   - Run the Ansible playbook to deploy/update the app

---

##  Setup & Configuration

### 1. Clone the Repository

```
git clone 
cd 
```


### 2. Create Azure Infrastructure (Terraform)
```
cd terraform
terraform init
terraform apply
```


> This creates the Azure VM and prints the public IP address.


### 3. Prepare Flask App and Dockerfile

- `app.py` is a basic Flask application
- `Dockerfile` builds a container using Python
- `requirements.txt` installs Flask

---

### 4. Configure Ansible

Edit `ansible/inventory.ini` with Azure VM IP:

```ini
[azure_vm]
<public-ip> ansible_user=azureuser ansible_ssh_private_key_file=~/.ssh/id_rsa
```

Run the playbook:

```bash
ansible-playbook -i inventory.ini ansible/docker.yml
```

---

### 5. Setup GitHub Actions

Create two **GitHub Secrets**:

| Secret Name | Description                           |
|-------------|---------------------------------------|
| `SSH_KEY`   |  private SSH key (`id_rsa`) |
| `HOST`      | Public IP of  Azure VM                |

GitHub Actions will:
- Checkout the repo
- Install Ansible on the runner
- SSH into Azure VM and run your playbook

---

### 6. Access the App

Visit  public VM IP:

```
http://74.235.0.167/

```
### 7. Output Screenshot
[sample App](./sample-application/Screenshot (95).png)

