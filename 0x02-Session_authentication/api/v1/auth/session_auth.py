#!/usr/bin/env python3

"""
Handles session authorization and authentication

Author: Bradley Dillion Gilden
Date: 14-02-2024
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """Handles session authorization and authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a Session ID for a user_id
        """
        if (user_id is None or type(user_id) is not str):
            return None
        session_id = str(uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id 
