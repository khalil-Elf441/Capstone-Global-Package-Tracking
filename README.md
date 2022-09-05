[![CircleCI](https://dl.circleci.com/status-badge/img/gh/khalil-Elf441/Capstone-Global-Package-Tracking/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/khalil-Elf441/Capstone-Global-Package-Tracking/tree/master)

# Capstone-Global-Package-Tracking

Global package traking (GPT) provides end-to-end inbound and outbound item tracking, helps to plan, implement, and control the movement and storage of goods, services, or information within a supply chain and between the points of origin and consumption.


## Overview

In this project I applied the skills and knowledge which were developed throughout the Cloud DevOps Nanodegree program. These included:

- Working in AWS
- Using CircleCI to implement Continuous Integration and Continuous Deployment
- Building pipelines
- Working with CloudFormation to deploy clusters
- Building Docker containers in pipelines
- Building Kubernetes clusters


## Application
The Application is based on a python3 script using flask to render a simple webpages in the user's browse.

### File description 

```
├───.circleci
├───CloudFormation
├───gpt_app
│   ├───static
│   │   ├───css
│   │   │   └───bootstrap
│   │   ├───fonts
│   │   │   ├───flaticon
│   │   │   │   ├───font
│   │   │   │   └───license
│   │   │   └───icomoon
│   │   │       ├───demo-files
│   │   │       └───fonts
│   │   ├───images
│   │   ├───js
│   │   └───scss
│   │       └───bootstrap
│   │           ├───mixins
│   │           ├───utilities
│   │           └───vendor
│   └───template
├───k8s
└───screenshots
```


## Getting Started

### Prerequisites
- AWS account
- Install and configure the necessary plugins : aws, git, docker, kubectl, eksctl

### Setup
Create EKS cluster by running the command below: 
```sh
eksctl create cluster -f CloudFormation/create-cluster.yml 
```
### Configure CircleCi environment variables

```sh
AWS_ACCESS_KEY_ID		
AWS_DEFAULT_REGION		
AWS_SECRET_ACCESS_KEY		
DOCKERHUB_PASSWORD		
DOCKERHUB_USERNAME		
DOCKER_IMAGE_NAME	
```

Run the CircleCi pipeline.

Make sure that your the local kubernetes this up-to-date with the aws eks cluster by running the command below :

```sh
aws eks update-kubeconfig --region us-west-2 --name gpt-app
```

## Check deployment

```sh
kubectl get svc,po,deploy
```

![4-Check-deployment.PNG](4-Check-deployment.PNG "4-Check-deployment.PNG")

## Running Web APP

![6-gpt-web-app-access.PNG](6-gpt-web-app-access.PNG "6-gpt-web-app-access.PNG")
