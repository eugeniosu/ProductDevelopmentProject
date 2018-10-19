Backend
===============================
At this stage, the infrastructure and resources should be created in AWS. We need to use the OutputKeys obtained by cloudformation script.

Make sure you are in `/backend` directory and  virtualenv is activated.

Tests
----------
Since the database was created in a private subnet, it's not possible to run test against it. 
We need to have a reachable database and configure a dev environment to run both model and view tests. 

First task is to modify the file 'ProductDevelopmentProject/settings/production.py' with your own database. 

Run Tests	
```
./manage.py test --settings=ProductDevelopmentProject.settings.development
```

Initial Deployment
----------

Install the requirements.
```
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
Zappa will automatically create an AWS API gateway and will provide an URL that will  appear at the end of the script. Copy and save **just the domain** of this URL. It is required for the next step (API_GATEWAY).

Final Deployment
----------

Edit the file `ProductDevelopmentProject/settings/production.py` with the next values:

[ALLOWED_HOST] = API_GATEWAY

| `production.py` | AWS OutputKey| AWS Original Configuration|
| ------| ------ | ------ |
| [DBEndpoint] | DataBaseEndpoint |-|
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
