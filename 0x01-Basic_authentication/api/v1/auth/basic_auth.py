#!/usr/bin/env python3

"""
Handles base64 strings in Authorization header

Author: Bradley Dillion Gilden
Date: 12-02-2024
"""
import base64
from typing import TypeVar


class BasicAuth:
    """ Handles base64 strings in Authorization header
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Extracts the base64 token
        """
        if (authorization_header is None):
            return None
        elif (type(authorization_header) is not str):
            return None
        elif (authorization_header.startswith("Basic ") is False):
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ returns the decoded value of a Base64 string
        """
        if (base64_authorization_header is None):
            return None
        elif (type(base64_authorization_header) is not str):
            return None
        try:
            data = base64.b64decode(base64_authorization_header)
            return data.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> (str, str):
        """ returns the user email and password from the Base64 decoded value
        """
        if (decoded_base64_authorization_header is None):
            return (None, None)
        elif (type(decoded_base64_authorization_header) is not str):
            return (None, None)
        elif (":" not in decoded_base64_authorization_header):
            return (None, None)
        else:
            return tuple(decoded_base64_authorization_header.split(":"))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ returns the User instance based on his email and password.
        """
        if (user_email is None or type(user_email) is not str):
            return None
        elif (user_pwd is None or type(user_pwd) is not str):
            return None
