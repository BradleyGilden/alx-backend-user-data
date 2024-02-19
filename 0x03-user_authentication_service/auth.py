#!/usr/bin/env python3

"""
This module handles user authentication

Author: Bradley Dillion Gilden
Date: 19-02-2024
"""
import bcrypt


def _hash_password(password):
    """ hashes password using the bcrypt module
    """
    return bcrypt.hashpw(password.encode(),
                         b'$2b$12$lzjRlDFwx6/qdBwDgnIkd.')
