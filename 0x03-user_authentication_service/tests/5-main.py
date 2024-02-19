#!/usr/bin/env python3

"""
<module docstring>

Author: Bradley Dillion Gilden
Date: 19-02-2024
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__name__)))
from auth import Auth


email = 'me@me.com'
password = 'mySecuredPwd'

auth = Auth()

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))
