#!/usr/bin/env python3

"""
This module handles user authentication

Author: Bradley Dillion Gilden
Date: 19-02-2024
"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """ hashes password using the bcrypt module
    """
    return bcrypt.hashpw(password.encode(),
                         b'$2b$12$lzjRlDFwx6/qdBwDgnIkd.')


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ registers a new user to the database
        """
        try:
            self._db.find_user_by(email=email)
            # if no exception is raised, means user already exists
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
