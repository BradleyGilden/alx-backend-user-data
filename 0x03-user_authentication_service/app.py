#!/usr/bin/env python3

"""
This module contains the routes to the flask application

Author: Bradley Dillion Gilden
Date: 19-02-2024
"""
from flask import Flask, jsonify, request
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def home():
    """ simple home route
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user():
    """ registers user data
    """
    fields = request.form

    try:
        user = AUTH.register_user(fields.get("email"), fields.get("password"))
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
