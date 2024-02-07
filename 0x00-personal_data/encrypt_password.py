#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 07-02-2024
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Salted pass generation
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ validated password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
