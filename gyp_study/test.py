# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def is_valid_email(addr):
    if re.match(r'^\w+\.\w+?@\w+\.com', addr):
        return True
    else:
        return False
