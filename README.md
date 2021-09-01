# FSND Capstone Project 

### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

 - [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

### Running the server

From within the root directory

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```
To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
   - in API Settings:
     - Enable RBAC
     - Enable Add Permissions in the Access Token
5. Create new API permissions:
   - `get:actors`
   - `get:movies`
   - `post:actors`
   - `post:movies`
   - `patch:actors`
   - `patch:movies`
   - `delete:actors`
   - `delete:movies`
6. Create new roles for:
   - Casting Assistant
     - can `get:actors`,`get:movies`,`post:actors`,`delete:actors`,`patch:actors`,`patch:movies`
   - Casting Director
     - can `get:actors`,`get:movies`
    - Executive Producer
     - can perform all actions
7. Test the endpoints with [Postman](https://getpostman.com).
   - Register 3 users - assign the Casting Assistant role to one and Casting Director role to the other and Executive Producer role to the last.
   - Sign into each account and make note of the JWT.
   - Test the endpoints by using : https://capstone-project-fsnd-program.herokuapp

## Running the API
API endpoints have been deployed successfully and can be accessed via: https://capstone-project-fsnd-program.herokuapp.com
Auth0 information that is required to authorized access for endpoints can be found in setup.sh

## API Reference 

### Error Handling
Errors are returned as JSON objects in the following format:
```
 {
   "success": False, 
   "error": 404,
   "message": "resource not found"
 }
```
The API will return four error types when requests fail:

 -400: Bad Request

 -404: Resource Not Found

 -422: Not Processable
 
 -401: Method Not Allowed

### Endpoints

**GET '/'**

 **General**
   - Request Arguments: None
   - Returns: Returns greeting message. 

 ```
 {
    "message": "Hello world!, This is capstone project",
    "success": true
}
```

**GET '/actors'**

 **General** 
 - Request Arguments: None
 - Returns: An object with all available actors

 ```
 {
    "actors": [
        {
            "age": 0,
            "gender": "Female",
            "id": 1,
            "name": "actor test name"
        },
        {
            "age": 45,
            "gender": "Female",
            "id": 2,
            "name": "actor test name 2"
        },
        {
            "age": 45,
            "gender": "Female",
            "id": 3,
            "name": "actor test name 3"
        },
        {
            "age": 45,
            "gender": "Female",
            "id": 4,
            "name": "actor test name 4"
        },
        {
            "age": 45,
            "gender": "Female",
            "id": 5,
            "name": "actor test name 4"
        }
    ],
    "success": true
}
```
**GET/movies**

 **General**
   - Request Arguments: None
   - Returns: An object with all available movies.

  ```
  {
    "movies": [
        {
            "id": 1,
            "release date": "Tue, 12 Dec 2000 00:00:00 GMT",
            "title": "movie test title1"
        },
        {
            "id": 2,
            "release date": "Tue, 12 Dec 2000 00:00:00 GMT",
            "title": "movie test title2"
        },
        {
            "id": 3,
            "release date": "Tue, 12 Dec 2000 00:00:00 GMT",
            "title": "movie test title3"
        },
        {
            "id": 4,
            "release date": "Tue, 12 Dec 2000 00:00:00 GMT",
            "title": "movie test title4"
        },
        {
            "id": 5,
            "release date": "Tue, 12 Dec 2000 00:00:00 GMT",
            "title": "movie test title5"
        }
    ],
    "success": true
  }
  ```

**POST/actors**

 **General**
   - Request Arguments: name-string, age-integer, gender-string.
   - Returns: The object of the created actor. 

   ```
    {
    "new_actor": {
        "age": 45,
        "gender": "Female",
        "id": 6,
        "name": "actor test name 4"
    },
    "success": true
  }
   ```

**POST/movies**

 **General**
   - Request Arguments: title-string, release date-string with date "yyyy-mm-dd"
   - Returns: The object of the created movie. 

   ```
   {
    "new_movie": {
        "id": 6,
        "release date": "Tue, 12 Dec 2000 00:00:00 GMT",
        "title": "movie test name"
    },
    "success": true
   }
   ```

**DELETE/actors/{actor_id}**

 **General**
   - Request Arguments: id-integer
   - Returns: The id of the deleted actor. 
   ```
   {
    "deleted_id": 4,
    "success": true
   }
   ```

**DELETE/movies/{movie_id}**

 **General**
   - Request Arguments: id-integer
   - Returns: The id of the deleted movie. 
   ```
   {
    "deleted_id": 4,
    "success": true
   }
   ```

**PATCH/actors/{actor_id}**

 **General**
   - Request Arguments: id-integer
   - Returns: The object of the updated actor. 
   ```
   {
    "success": true,
    "updated_actor": {
        "age": 33,
        "gender": "Female",
        "id": 5,
        "name": "actor test name 4"
    }
    }
   ```

**PATCH/movies/{movie_id}**

 **General**
   - Request Arguments: id-integer
   - Returns: The object of the updated movie. 
   ```
   {
    "success": true,
    "updated_movie": {
        "id": 5,
        "release date": "Tue, 12 Dec 2000 00:00:00 GMT",
        "title": "updated test movie title"
    }
   }
   ```

## Testing
To run the tests, run
```
python test_app.py
```
