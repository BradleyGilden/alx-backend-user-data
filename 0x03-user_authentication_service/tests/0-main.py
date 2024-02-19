#!/usr/bin/env python3

"""
<module docstring>

Author: Bradley Dillion Gilden
Date: 19-02-2024
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__name__)))
from user import User

print(User.__tablename__)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))
