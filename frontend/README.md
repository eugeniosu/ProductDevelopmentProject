Frontend
===============================
Make sure you are in `/frontend` directory.

Configuration
----------

Edit the config section in  `package.json` and replace the following value with right  AWS outputkey:


| `package.json` | AWS OutputKey|
| ------| ------ |
| [S3_WebpageBucket] | WebsiteBucket |


![Alt text](https://github.com/eugeniosu/ProductDevelopmentProject/blob/master/readme-images/packagejsonconf.jpg?raw=true)


Modify the file `config/prod.env.js` and put API_GATEWAY retrieved from the backend deployment

| `package.json` | Zappa deployment|
| ------| ------ |
| [API] | API_GATEWAY |


![Alt text](https://github.com/eugeniosu/ProductDevelopmentProject/blob/master/readme-images/vueconf.jpg?raw=true)


Install dependencies
```
$ npm install
```

Tests
----------
Start selenium server
```
$ npm run e2e
```

Deployment
----------

Deploy the frontend
```
$ npm run deploy-prod
```
After this step, S3 bucket should be hosting the website.
Finally, we have to go to the browser and paste the url returned by  AWS OutputKey: `CloudfrontEndpoint`

### Todos
 - Write MORE Tests
