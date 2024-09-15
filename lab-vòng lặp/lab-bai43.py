# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:25:36 2024

@author: Lenovo
"""

n=int(input("Nhập n:"))
S=0
for i in range(1,n+1):
    S+=i/(i+1)
print("1/2+2/3+..+ n/n+1",S)