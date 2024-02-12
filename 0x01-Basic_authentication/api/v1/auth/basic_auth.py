#!/usr/bin/env python3

"""
Handles base64 strings in Authorization header

Author: Bradley Dillion Gilden
Date: 12-02-2024
"""
import base64


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
