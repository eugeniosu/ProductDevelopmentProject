BackEnd
===============================
At this stage, the infrastucture should created in AWS. We need to use the OutputKeys obtained by cloudformation script.

Make sure you are in `/backend` directory and  virtualenv is activated.

Initial Deployment
----------

Install the requirements.
```
$ pip install -r requirements/requirementsProd.txt
```

Edit the file `zappa_settings.json` with the OutputValues from AWS resources.

| `zappa_settings.json` | AWS OutputKey|
| ------| ------ |
| [s3_zappa] | ZappaS3Bucket |
| [Subnet1] | PrivateSubnet1 |
| [Subnet2] | PrivateSubnet2 |
| [SecurityGroup] | SecurityGroup |


Do the initial deployment
```
$ zappa deploy prod
```
Zappa will automaticly create an AWS API gateway and will provide an URL that will  appear at the end of the script. Copy and save **just the domain** of this URL. It is required for the next step (API_GATEWAY).


Edit the file `ProductDevelopmentProject/settings/production.py` with the next values:

[ALLOWED_HOST] = API_GATEWAY

| `production.py` | AWS OutputKey| AWS Original Configuration|
| ------| ------ | ------ |
| [DBEndpoint] | DataBaseEndpoint |-|
| [DBUsername] | - |DBUsername|
| [DBPassword] | - |DBPassword|
| [DBName] | - |DBName|


Final Deployment
----------
Just execute the next two commands and he backend configuration will be complete
```
$ zappa update prod
$ zappa manage prod migrate
