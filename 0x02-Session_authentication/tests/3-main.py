#!/usr/bin/env python3
""" Main 2
"""
import sys
import os
from flask import Flask, request
sys.path.append(os.path.dirname(os.path.abspath(__name__)))
from api.v1.auth.auth import Auth

auth = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """ Root path
    """
    return "Cookie value: {}\n".format(auth.session_cookie(request))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
