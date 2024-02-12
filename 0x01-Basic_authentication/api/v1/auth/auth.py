#!/usr/bin/env python3

"""
Manages the API authentication.

Author: Bradley Dillion Gilden
Date: 12-02-2024
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ a class to manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """unknown functionality"""
        return False

    def authorization_header(self, request=None) -> str:
        """the Flask request object"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """the Flask request object"""
        return request
