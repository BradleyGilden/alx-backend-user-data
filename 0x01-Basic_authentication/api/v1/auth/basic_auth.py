#!/usr/bin/env python3

"""
Handles base64 strings in Authorization header

Author: Bradley Dillion Gilden
Date: 12-02-2024
"""


class BasicAuth:
    """"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
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
