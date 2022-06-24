# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import unittest
class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def get_grade(self):
        # try:      
        #     if self.score >= 80:
        #         return 'A' 
        #     elif self.score >= 60:
        #         return 'B'
        #     else:
        #         return 'C'
        # except ValueError:
        #     raise ValueError('score must beween 0~100')
        if not isinstance(self.score, (int, float)) or self.score < 0 or self.score >100:
            raise ValueError('score must between 0~100')  
        if self.score >= 80:
            return 'A' 
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'    
