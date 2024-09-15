# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:23:41 2024

@author: Lenovo
"""

n=int(input("Nhập số n:"))
S=0
for i in range(2,2*n+1,2):
    S+=1/i
print("S=1/2+..+1/{2*n}=",S)