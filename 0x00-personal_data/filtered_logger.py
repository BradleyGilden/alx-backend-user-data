#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 07-02-2024
"""
import re
from typing import List


def filter_datum(fields: List, redaction: str, message: str,
                 separator: str) -> str:
    """obfuscates log messages depending given paramenters"""
    filter = message
    for field in fields:
        filter = re.sub(r'(?<={fld}\=)[^{sp}]+(?={sp})'
                        .format(sp=separator, fld=field), redaction, filter)
    return filter
