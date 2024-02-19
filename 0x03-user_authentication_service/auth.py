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
from uuid import uuid4
from typing import Union


def _hash_password(password: str) -> bytes:
    """ hashes password using the bcrypt module
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


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

    def valid_login(self, email: str, password: str) -> bool:
        """ checks for valid password
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False

    def _generate_uuid(self) -> str:
        """ generate random uuid's
        """
        return str(uuid4())

    def create_session(self, email: str) -> Union[str, None]:
        """ creates session id's for a user using their email
        """
        try:
            user = self._db.find_user_by(email=email)
            sid = self._generate_uuid()
            self._db.update_user(user.id, session_id=sid)
            return sid
        except NoResultFound:
            return None
