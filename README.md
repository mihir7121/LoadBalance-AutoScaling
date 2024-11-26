# LoadBalance-AutoScaling with Minikube

This guide walks you through installing Docker and Minikube on Ubuntu, configuring the environment, and starting a Minikube cluster with load balancing and auto-scaling capabilities.

---

## Prerequisites

1. **Operating System**: Ubuntu Linux 20.04.4 LTS (used for this demo)
2. **Docker**: Ensure Docker is installed and running
   ```bash
   sudo apt-get install docker.io
   sudo usermod -aG docker $USER
   sudo systemctl start docker
   sudo systemctl enable docker
    ```
3. **Kubernetes components**: Install using snap
    ```bash
    sudo snap install kubeadm kubelet kubectl 
    ```

## Installation guidelines
1. **Clone the Git repo**:
```bash
git clone https://github.com/mihir7121/LoadBalance-AutoScaling.git
cd LoadBalance-AutoScaling/
```

1. **Install Minikube**:
Download the Minikube binary for x86-64 architecture:
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```
Documentation for Minikube can be found [here](https://minikube.sigs.k8s.io/docs/start/)

2. **Start the Minikube Cluster**:
Start a Minikube cluster using Docker as the driver with a memory allocation of 4096 MB:

```bash
minikube start --driver=docker --memory=4096
eval $(minikube docker-env)
```

3. **Enable Required Add-ons**:
Enable essential services for monitoring and API gateway:
```bash
minikube addons enable metrics-server
minikube addons enable ingress
```
4. **Create a docker image for our app.py**:
```bash
docker build -t flask-app:latest .
```
5. **Install Locust for Testing**:
Locust is used for load testing. Install it using pip:
```bash
pip install locust 
```

6. **Apply YAML Configurations for Kubernetes Resources**:
Apply all the YAML configuration files to create and manage the Kubernetes resources, such as deployments, services, pods etc.:   
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
kubectl apply -f autoscaler.yaml
```
7. **Find your minikube IP**:
This is essential for locust testing
```bash
minikube ip
```

8. **Launch Supporting Tools**:
Open three separate terminals to run the following commands
* Terminal 1: Start the Minikube tunnel
```bash
minikube tunnel
```

* Terminal 2: Launch the Minikube dashboard
```bash
minikube dashboard
```

* Terminal 3: Start Locust
```bash
locust
```

---

## How to Use

When you execute the locust command, it will open up a server on http://127.0.0.1:8089
Specify the concurrent users you require, along with the spike speed and the `minikube ip` as the host.

![Locust Home Screen](/locust.png "Locust Home Screen")

A dashboard should open when you execute `minikube dashboard` which enables users to monitor cluster activities.

---

## Notes
- Use the Minikube dashboard to monitor the cluster and view resource utilization.
- Use Locust to generate and analyze traffic load on your applications.
- If Docker is not running, start it with:
```bash
sudo systemctl start docker
```
- To stop the Minikube cluster:
```bash
minikube stop
```
- To delete the cluster entirely:
```bash
minikube delete
```

- Check Minikube logs for troubleshooting
```bash
minikube logs
```