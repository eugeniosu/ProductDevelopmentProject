ProductDevelopmentProject
==============================
ProductDevelopmentProject is a solution that allows insurance companies to define their own custom model without having a rigid model. 

It's composed of two main parts: backend and frontend.  they are independent each other and the integration is via REST API's. 


# Technologies 
Backend:
* [Django Rest] - Django REST framework is a powerful and flexible toolkit for building Web APIs.
* [PostgreSQL] - PostgreSQL is a powerful, open source object-relational database system.
* [Psycopg] - Psycopg is the most popular PostgreSQL adapter for the Python programming language
* [Zappa] - Zappa makes it super easy to build and deploy server-less, event-driven Python applications on AWS Lambda + API Gateway.

Frontend:
*  [vue.js] - A progressive, incrementally-adoptable JavaScript framework for building UI on the web.
*  [node.js] - evented I/O for the backend.


   [Django Rest]: <https://www.django-rest-framework.org/>
   [PostgreSQL]: <https://www.postgresql.org/>
   [Psycopg]: <http://initd.org/psycopg/>
   [Zappa]: <https://github.com/Miserlou/Zappa/>
   [node.js]: <http://nodejs.org>
   [Vue.js]: <https://vuejs.org/>
//TODO: list all tecs
# Infrastructure Creation.
This application runs on Amazon Web Services (AWS). Consequently, a CloudFormation yaml file is provided to generate all the resources needed.

Edit cloudformation.yml file and set the next parameters:
* [EnvironmentName] -  An environment name that will be prefixed to resource names
* [DbUsername] - User for accessing the database
* [DbPassword] - Password for accessing the database 

Install `aws-cli`:
```
 $ pip install aws-cli
```
Configure `aws-cli`. The AWS CLI will prompt you for four pieces of information. AWS Access Key ID and AWS Secret Access Key are your account credentials.
```
 $ aws configure
```
Execute the yaml file using `aws-cli`(This process is going to take several minutes to complete)
```
 $ aws cloudformation create-stack --stack-name ProductDevelopmentStack --template-body file://cloudformation.yml
```

All the resources needed in this project were generated in the previous process. Thus, check and save them in safe place.
```
 $ aws cloudformation describe-stacks --stack-name ProductDevelopmentStack
```
