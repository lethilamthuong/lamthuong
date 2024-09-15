# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:40:41 2024

@author: Lenovo
"""
 
#a
print("a")
j = 0
for i in range(0, 10):
    j += i
print(j)
#b
print()
print("b")
j = 1
for i in range(0, 10):
    j += j
    print(j)
#c
print()
print("c")
for j in range(0, 10):
    j += j
    print(j)

