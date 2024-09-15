# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:20:55 2024

@author: Lenovo
"""

n=int(input("Nhập n:"))
S=0 
for i in range(1,n+1):
  S+=1/i
print("S=1+ 1/2 + 1/3+..+ 1/n =",S)