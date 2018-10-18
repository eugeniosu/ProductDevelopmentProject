FrontEnd
===============================

Configuration
----------

Edit the config section in  `package.json` and replace the following value with right  AWS outputkey:


| `package.json` | AWS OutputKey|
| ------| ------ |
| [S3_WebpageBucket] | - |

Modify the file `config/prod.env.js` with API_URL retrieved from the backend deployment
| `package.json` | Zappa deployment|
| ------| ------ |
| [API] | API_URL |


Deployment
----------

install dependencies
```
$ npm install
```

Deploy the frontend
```
$ npm run deploy-prod
```
After this step, S3 bucket should be housting the website.
Finally, we have to the browswer and paste the url provided, which is AWS OutputKey
