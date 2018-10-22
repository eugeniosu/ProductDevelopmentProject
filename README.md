ProductDevelopmentProject
==============================
ProductDevelopmentProject is a solution that allows insurance companies to define their own custom model. 

It's composed of two main parts: backend and frontend. They are independent each other and they are integrated via REST API's. 


Technologies 
----------
For both local deployments we will use [Docker] containers

Backend:
* [pytest] - The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.
* [Django Rest] - Django REST framework is a powerful and flexible toolkit for building Web APIs.
* [PostgreSQL] - PostgreSQL is a powerful, open source object-relational database system.
* [Psycopg] - Psycopg is the most popular PostgreSQL adapter for the Python programming language
* [Zappa] - Zappa makes it super easy to build and deploy server-less, event-driven Python applications on AWS Lambda + API Gateway.

Frontend:
*  [Nightwatch] - Write efficient and straightforward end-to-end tests in Node.js which run against a Selenium/WebDriver server.
*  [vue.js] - A progressive, incrementally-adoptable JavaScript framework for building UI on the web.
*  [node.js] - evented I/O for the backend.


   [Django Rest]: <https://www.django-rest-framework.org/>
   [PostgreSQL]: <https://www.postgresql.org/>
   [Psycopg]: <http://initd.org/psycopg/>
   [Zappa]: <https://github.com/Miserlou/Zappa/>
   [node.js]: <http://nodejs.org>
   [Vue.js]: <https://vuejs.org/>
   [Docker]: <https://www.docker.com/>
   [Nightwatch]: <http://nightwatchjs.org/>
   [pytest]: <https://docs.pytest.org/en/latest/>


Quick Deployment 
----------
You can setup a local environment using Docker if you are eager to see the application in action. 

Start the backend.	
```
$ docker-compose -f backend/docker-compose.yml up --build
```

Start the frontend.	
```
$ docker-compose -f frontend/docker-compose.yml up --build
```


# Configure Production Environment in AWS

Create a virtualenviroment.
```
$ virtualenv env -p python3
```
Active the Environment
```
$ source env/bin/activate
```

Infrastructure Creation.
----------

This application runs on Amazon Web Services (AWS). Consequently, a CloudFormation yaml file is provided to generate all the resources needed.

Edit `cloudformation.yml` file and set the next parameters:
* [EnvironmentName] -  An environment name that will be prefixed to resource names
* [DBName] - Database name
* [DBUsername] - User for accessing the database
* [DBPassword] - Password for accessing the database 

`cloudformation.yml` file should like this:
![Alt text](https://github.com/eugeniosu/ProductDevelopmentProject/blob/master/readme-images/cloudformationconf.jpg?raw=true)

Install `aws-cli`:
```
$ pip install awscli
```
Configure `aws-cli`. The AWS CLI will prompt you for four pieces of information. AWS Access Key ID and AWS Secret Access Key are your account credentials. For this deployment we will be using `us-east-1` region.
```
$ aws configure
```
Execute the yaml file using `aws-cli`(This process is going to take several minutes to complete)
```
$ aws cloudformation create-stack --stack-name ProductDevelopmentStack --template-body file://cloudformation.yml
```

Getting AWS OutputKeys.
----------

All the resources needed to make this project run were generated in the previous step.
Run the next command to find out OutputValues and save them in a safe place.
```
$ aws cloudformation describe-stacks --stack-name ProductDevelopmentStack
```

![Alt text](https://github.com/eugeniosu/ProductDevelopmentProject/blob/master/readme-images/outputKey.jpg?raw=true)

Next Steps
----------
The next steps must be done in the given order.
1. [Deploy backend](https://github.com/eugeniosu/ProductDevelopmentProject/tree/master/backend)
2. [Deploy frontend](https://github.com/eugeniosu/ProductDevelopmentProject/tree/master/frontend)
