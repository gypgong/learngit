# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

obj = dict(name='小明', age=20)
s = json.dumps(obj)
print(s)


obj = dict(name='小明', age=20)
s1 = json.dumps(obj, ensure_ascii=False)
print(s1)

obj = dict(name='小明', age=20)
s2 = json.dumps(obj, ensure_ascii=True)
print(s2)

