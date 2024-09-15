# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:27:31 2024

@author: Lenovo
"""

A = 2
B = 7
C = 9
D = 979
for x in range(1, D // A + 1): 
    for y in range(1, (D - A * x) // B + 1): 
        z = (D - A * x - B * y) // C 
        if (D - A * x - B * y) % C == 0 and z > 0: 
            print(x, y, z)