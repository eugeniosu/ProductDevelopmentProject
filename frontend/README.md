# Configure Environment 
Create a virtualenviroment.
```
$ virtualenv env -p python3
```

Install the requirements.
```
$ pip install -r requirements/production.txt
```

#  Initial Deployment
Edit the file `zappa_settings.json` with the OutputValues from AWS resources.

| `zappa_settings.json` | AWS OutputKey|
| ------| ------ |
| [s3_bucket] | ZappaS3Bucket |
| [Subnet1] | PrivateSubnet1 |
| [Subnet2] | PrivateSubnet2 |

Do the initial deployment
```
$ zappa deploy prod
```
Zappa will automaticly create an AWS API gateway and will provide an URL that will  appear at the end of the script. Copy and save **just the domain** of this URL. It is required for the next step (API_GATEWAY).

Edit the file `/ProductDevelopmentProject/settings/production.py` with the next values:

[ALLOWED_HOSTS] = API_GATEWAY

| `production.py` | AWS OutputKey| AWS Original Configuration|
| ------| ------ | ------ |
| [DBEndpoint] | DataBaseEndpoint |-|
| [DBUsername] | - |DBUsername|
| [DBPassword] | - |DBPassword|
| [DbName] | - |DBName|

Create new migrations based on the models.
```
$ zappa manage prod makemigrations
```

# Tests
Run the test for both models and views
```
$ zappa manage prod tests
```

#  Final Deployment
Just execute the next two commands and he backend configuration will be complete
```
$ zappa update prod
$ zappa manage prod migrate
