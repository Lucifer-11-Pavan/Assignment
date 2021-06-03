# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 19:28:19 2021

@author: Lucifer
"""

def uniqueCode(pic_name):
    code = ''
    for character in pic_name:
        if character.isdigit():
            code = code + character
    return code

uniqueCode('paul-12345.jpg')