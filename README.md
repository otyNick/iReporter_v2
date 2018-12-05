[![Build Status](https://travis-ci.org/otyNick/iReporter_v2.svg?branch=master)](https://travis-ci.org/otyNick/iReporter_v2)
[![codecov](https://codecov.io/gh/otyNick/iReporter_v2/branch/master/graph/badge.svg)](https://codecov.io/gh/otyNick/iReporter_v2)

# Project : iReporter
Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

To view postman collection


**How it works**  
A users can :
```
1. Create an account and log in
2. Create intervention -a call for a government agency to intervene- record
3. Edit or delete their red-flag or intervention records.
4. Add or edit geolocation (Lat Long Coordinates) to their red-flag or intervention records.
5. Add images or videos to their red-flag or intervention records, to support their claims.
6. Get real-time email or SMS notification when Admin changes the status of their record.
```
- Admin can change the status of a record to either  
under investigation,  
rejected (in the event of a false claim)  
or resolved (in the event that the claim has been investigated and resolved).

- The application displays a Google Map with Marker showing the red-flag or intervention location.




## Installation and Deployment.

**Clone the repo**

```.env
https://github.com/otyNick/iReporter_v2.git
```

**Setup environment**

Create a virtual environment and activate it
 ```.env
 python3 - m venv env
 ```
 Create a ```.env``` file in the parent directory and add this:
 ```..env
 source env/bin/activate

 export FLASK_APP=run.py
       FLASK_CONFIG="development"
       FLASK_ENV=development
       FLASK_DEBUG=1
       JWT_SECRET_KEY="2fd4e1c67a2d28fced849ee1bb76e7391b93eb12"
 ```
 To initialize flask environment and add environment variables to it run:
 ```.env
 source .env
 ```
 Install all the dependencies needed by
 ```..env
 pip install - r requirements.txt
 ```
 **Run the application**

 Run the flask application
 ```.env
  flask run
 ```

**Test the application**
 ```.env
flask test
or
flask cov
```

## Endpoints to test

| Method | Endpoint                                    | Description                                    |
| ------ | ------------------------------------------- | ---------------------------------------------- |
| POST   | /api/v1/auth/signup                         | sign up a user                                 |
| POST   | /api/v1/auth/login                          | login a user                                   |
| POST   | /api/v1/red-flags                           | Create a red-flag record.                      |
| GET    | /api/v1/red-flags                           | Fetch all red-flag records.                    |
| GET    | /api/v1/red-flags/<red-flag-id>             | Fetch a specific red-flag record.              |
| PATCH  | /api/v1/red-flags/<red-flag-id>/location    | Edit the location of a specific record.        |
| PATCH  | /api/v1/red-flags/<red-flag-id>/comment     | Edit the comment of a specific record.         |
| DELETE | /api/v1/red-flags/<red-flag-id>             | Delete a specific red flag record.             |

### Author

Nicholas Otieno
