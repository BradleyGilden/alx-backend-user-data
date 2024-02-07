#!/usr/bin/env python3

"""
Testing filter_datum

Author: Bradley Dillion Gilden
Date: 07-02-2024
"""
import os
import sys
import logging

sys.path.append(os.path.abspath(os.path.abspath(__file__) + "/../../"))

from filtered_logger import RedactingFormatter


if __name__ == '__main__':
    message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
    log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
    formatter = RedactingFormatter(fields=("email", "ssn", "password"))
    print(formatter.format(log_record))
