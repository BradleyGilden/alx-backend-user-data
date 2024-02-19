# User authentication service

In the industry, you should not implement your own authentication system and use a module or framework that doing it for you (like in Python-Flask: Flask-User). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing

## Learning Objectives

* How to declare API routes in a Flask app
* How to get and set cookies
* How to retrieve request form data
* How to return various HTTP status codes

## Tasks

* [user.py](user.py) - In this task you will create a SQLAlchemy model named User for a database table named users (by using the mapping declaration of SQLAlchemy).

  The model will have the following attributes:

  * id, the integer primary key
  * email, a non-nullable string
  * hashed_password, a non-nullable string
  * session_id, a nullable string
  * reset_token, a nullable string

* [db.py](db.py) - 

  ### Step 1

  Implement the add_user method, which has two required string arguments: email and hashed_password, and returns a User object. The method should save the user to the database. No validations are required at this stage.

  ### Step 2
  Implement the DB.find_user_by method. This method takes in arbitrary keyword arguments and returns the first row found in the users table as filtered by the method’s input arguments. No validation of input arguments required at this point.

  Make sure that SQLAlchemy’s NoResultFound and InvalidRequestError are raised when no results are found, or when wrong query arguments are passed, respectively.

  ### Step 3
  In this task, you will implement the DB.update_user method that takes as argument a required user_id integer and arbitrary keyword arguments, and returns None.

  The method will use find_user_by to locate the user to update, then will update the user’s attributes as passed in the method’s arguments then commit changes to the database.

  If an argument that does not correspond to a user attribute is passed, raise a ValueError.

* [auth.py](auth.py) -

  ### Step 1
  In this task you will define a _hash_password method that takes in a password string arguments and returns bytes.

  The returned bytes is a salted hash of the input password, hashed with bcrypt.hashpw.

  ### Step 2
  create an Auth class with a register_user method that registers a new user to the application database

  ### Step 3

  In this task, you will implement the end-point to register a user. Define a users function that implements the POST /users route.

  Import the Auth object and instantiate it at the root of the module as such:

* [app.py](app.py) - 

  ### Step 1
  Create a Flask app that has a single GET route ("/") and use flask.jsonify to return a JSON payload of the form: `{"message": "Bienvenue"}`

  ### Step 2
  In this task, you will implement the end-point to register a user. Define a users function that implements the POST /users route.

  Import the Auth object and instantiate it at the root of the module as such:
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
