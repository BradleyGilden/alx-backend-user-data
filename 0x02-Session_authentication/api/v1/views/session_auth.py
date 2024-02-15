#!/usr/bin/env python3

"""
Session views

Author: Bradley Dillion Gilden
Date: 14-02-2024
"""
from api.v1.views import app_views
from os import getenv
from flask import jsonify, request, abort
from models.user import User


@app_views.route("/auth_session/login", methods=["POST"],
                 strict_slashes=False)
def handle_session_login() -> str:
    """ implements session login, returns dict of user
    """
    email = request.form.get("email")
    pwd = request.form.get("password")
    user = None
    if (email is None):
        return jsonify({"error": "email missing"}), 400
    elif (pwd is None):
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({'email': email})
        if not users or users == []:
            return jsonify({"error": "no user found for this email"}), 404
        for u in users:
            if u.is_valid_password(pwd):
                user = u
        if (user is None):
            return jsonify({"error": "wrong password"}), 401
    except Exception:
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    cookie_response = getenv('SESSION_NAME')
    user_dict = jsonify(user.to_json())

    user_dict.set_cookie(cookie_response, session_id)
    return user_dict


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def session_logout() -> str:
    """ implements logout of session
    """
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
