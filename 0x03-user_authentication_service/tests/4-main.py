#!/usr/bin/env python3

"""
<module docstring>

Author: Bradley Dillion Gilden
Date: 19-02-2024
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__name__)))
from auth import _hash_password

print(_hash_password("Hello Holberton"))
