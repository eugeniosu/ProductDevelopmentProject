ProductDevelopmentProject
==============================
ProductDevelopmentProject is a solution that allows insurance companies to define their own custom model without having a rigid model. 

It's composed of two main parts: backend and frontend.  they are independent each other and the integration is via REST API's. 


# Tech 
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
* [DBName] - Database name
* [DBUsername] - User for accessing the database
* [DBPassword] - Password for accessing the database 

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
#backend
# Configure Environment 
Create a virtualenviroment.
```
$ virtualenv env -p python3
```

Install the requirements.
```
$ pip install -r requirements/production.txt
```

#  Deployment
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

the final step is to run the next three commands 
```
$ zappa manage prod makemigrations
$ zappa update prod
$ zappa manage prod migrate
```

| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

* [s3_bucket] -  An environment name that will be prefixed to resource names
* [DbUsername] - User for accessing the database
* [DbPassword] - Password for accessing the database 

# Tests
./manage.








**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   
   

# New Features!

  - Import a HTML file and watch it magically convert to Markdown
  - Drag and drop images (requires your Dropbox account be linked)


You can also:
  - Import and save files from GitHub, Dropbox, Google Drive and One Drive
  - Drag and drop markdown and HTML files into Dillinger
  - Export documents as Markdown, HTML and PDF

Markdown is a lightweight markup language based on the formatting conventions that people naturally use in email.  As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually* written in Markdown! To get a feel for Markdown's syntax, type some text into the left window and watch the results in the right.

### Tech

Dillinger uses a number of open source projects to work properly:

* [AngularJS] - HTML enhanced for web apps!
* [Ace Editor] - awesome web-based text editor
* [markdown-it] - Markdown parser done right. Fast and easy to extend.
* [Twitter Bootstrap] - great UI boilerplate for modern web apps

* [Express] - fast node.js network app framework [@tjholowaychuk]
* [Gulp] - the streaming build system
* [Breakdance](http://breakdance.io) - HTML to Markdown converter
* [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

### Installation

Dillinger requires [Node.js](https://nodejs.org/) v4+ to run.

Install the dependencies and devDependencies and start the server.

```sh
$ cd dillinger
$ npm install -d
$ node app
```

For production environments...

```sh
$ npm install --production
$ NODE_ENV=production node app
```

### Plugins

Dillinger is currently extended with the following plugins. Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------| ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| Github | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |


### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantanously see your updates!

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ node app
```

Second Tab:
```sh
$ gulp watch
```

(optional) Third:
```sh
$ karma test
```
#### Building for source
For production release:
```sh
$ gulp build --prod
```
Generating pre-built zip archives for distribution:
```sh
$ gulp build dist --prod
```
### Docker
Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
cd dillinger
docker build -t joemccann/dillinger:${package.json.version} .
```
This will create the dillinger image and pull in the necessary dependencies. Be sure to swap out `${package.json.version}` with the actual version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we simply map port 8000 of the host to port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart="always" <youruser>/dillinger:${package.json.version}
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

#### Kubernetes + Google Cloud

See [KUBERNETES.md](https://github.com/joemccann/dillinger/blob/master/KUBERNETES.md)


### Todos

 - Write MORE Tests
 - Add Night Mode

License
----

MIT


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>

