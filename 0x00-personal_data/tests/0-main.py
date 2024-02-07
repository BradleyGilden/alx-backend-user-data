#!/usr/bin/env python3

"""
Testing filter_datum

Author: Bradley Dillion Gilden
Date: 07-02-2024
"""
import os
import sys

sys.path.append(os.path.abspath(os.path.abspath(__file__) + "/../../"))

from filtered_logger import filter_datum


if __name__ == '__main__':
    fields = ["password", "date_of_birth"]
    messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

    for message in messages:
        print(filter_datum(fields, 'xxx', message, ';'))
