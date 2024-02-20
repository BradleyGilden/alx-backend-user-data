#!/usr/bin/env python3

"""
This module contains the routes to the flask application

Author: Bradley Dillion Gilden
Date: 19-02-2024
"""
from flask import Flask, jsonify, request, make_response, abort, redirect
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    """ simple home route
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def reg_user() -> str:
    """ registers user data
    """
    fields = request.form

    try:
        user = AUTH.register_user(fields.get("email"), fields.get("password"))
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """ creates a login session for a user if login details are correct
    """
    fields = request.form
    if (AUTH.valid_login(fields.get("email"), fields.get("password"))):
        email = fields["email"]
        sid = AUTH.create_session(email)
        resp = make_response(jsonify({"email": email, "message": "logged in"}))
        resp.set_cookie("session_id", sid)
        return resp
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> str:
    """ log out the system by destroying curret user session
    """
    sid = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(sid)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    else:
        abort(403)


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile() -> str:
    """ returns a users email data
    """
    user = AUTH.get_user_from_session_id(request.cookies.get("session_id"))
    if user:
        return jsonify({"email": user.email})
    else:
        abort(403)


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token() -> str:
    """ returns reset token in payload
    """
    email = request.form.get("email")
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token})
    except ValueError:
        abort(403)


@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password() -> str:
    """ resets password according to user reset token
    """
    email = request.form.get("email")
    token = request.form.get("reset_token")
    password = request.form.get("new_password")

    try:
        AUTH.update_password(token, password)
        return jsonify({"email": email, "message": "Password updated"})
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
