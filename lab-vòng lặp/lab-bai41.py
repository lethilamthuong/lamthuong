# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:24:07 2024

@author: Lenovo
"""

n=int(input("Nhập số n:"))
S=0
for i in range(1,2*n+2,2):
    S+=1/i
print("S=1+1/3+..+1/(2*{n}+1)=",S)