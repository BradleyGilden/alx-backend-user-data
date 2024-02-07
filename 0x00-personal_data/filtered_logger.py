#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 07-02-2024
"""
import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """obfuscates log messages depending given paramenters"""
    filter = message
    for field in fields:
        filter = re.sub(r'(?<={fld}\=)[^{sp}]+(?={sp})'
                        .format(sp=separator, fld=field), redaction, filter)
    return filter


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """formats the message of the log"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
