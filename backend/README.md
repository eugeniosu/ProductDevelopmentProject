Backend
===============================
Make sure you are in `/backend` directory

Local Deployment
----------
The local deployment is really easy. You just need to have Docker and Docker compose installed in your machine

Execute docker compose.	
```
$ docker-compose up --build
```

*This step is mandatory to run tests locally in the frontend.

# Tests
We will be using docker to mount a PostgreSQL database and run tests against it. Keep in mind that production database is in a private subnet and it cannot be accessed outside of the VPN.

Run Tests	
```
$ docker-compose run backend pytest
```

Initial Production Deployment
----------
At this stage, the infrastructure and resources should have been created in AWS. We need to use the OutputValues obtained by cloudformation script.

You also need to activate virtualenv.

Activate virtualenv and install the requirements.
```
$ source  ../env/bin/activate
$ pip install -r requirements/requirementsProd.txt
```

Replace the key values in `zappa_settings.json` with the OutputValues from AWS resources.

| `zappa_settings.json` | AWS OutputKey|
| ------| ------ |
| [s3_zappa] | ZappaS3Bucket |
| [Subnet1] | PrivateSubnet1 |
| [Subnet2] | PrivateSubnet2 |
| [SecurityGroup] | SecurityGroup |


Make sure  `zappa_settings.json` file is similar to this one:

![Alt text](https://github.com/eugeniosu/ProductDevelopmentProject/blob/master/readme-images/zappaconf.jpg?raw=true)



Do the initial deployment
```
$ zappa deploy prod
```
Zappa will automatically create an AWS API gateway and will provide an URL that will  appear at the end of the script. Copy and save this URL. It is required for the next step and for setting up the frontend. We will call it API_GATEWAY.

Final Production Deployment
----------

Edit the file `ProductDevelopmentProject/settings/production.py` with the next values:

[ALLOWED_HOST] = API_GATEWAY (**just the domain**)

| `production.py` | AWS OutputKey| AWS Original Configuration|
| ------| ------ | ------ |
| [DBEndpoint] | DataBaseEndpoint() |-|
| [DBUsername] | - |DBUsername|
| [DBPassword] | - |DBPassword|
| [DBName] | - |DBName|


This is how `production.py` should be:
![Alt text](https://github.com/eugeniosu/ProductDevelopmentProject/blob/master/readme-images/databaseconf.jpg?raw=true)

Just execute the next two commands, and the backend configuration will be complete
```
$ zappa update prod
$ zappa manage prod migrate
```

### Todos
 - Dockerize zappa
