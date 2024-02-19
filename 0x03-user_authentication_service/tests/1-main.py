#!/usr/bin/env python3

"""
<module docstring>

Author: Bradley Dillion Gilden
Date: 19-02-2024
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__name__)))
from db import DB
from user import User

my_db = DB()

user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
print(user_1.id)

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
print(user_2.id)
