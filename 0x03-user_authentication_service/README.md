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

* [db.py](db.py) - Implement the add_user method, which has two required string arguments: email and hashed_password, and returns a User object. The method should save the user to the database. No validations are required at this stage.
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
