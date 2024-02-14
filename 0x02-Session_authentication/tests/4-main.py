#!/usr/bin/env python3
""" Main 2
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__name__)))
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.extract_user_credentials(None))
print(a.extract_user_credentials(89))
print(a.extract_user_credentials("Holberton School"))
print(a.extract_user_credentials("Holberton:School"))
print(a.extract_user_credentials("bob@gmail.com:toto1234"))
