# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:25:56 2024

@author: Lenovo
"""

n=int(input("Nhập n:"))
S=0
for i in range(0,n+1):
    S+=(2*i+1)/(2*i+2)
print("1/2+3/4+..+ 2n+1/2n+2=",S)