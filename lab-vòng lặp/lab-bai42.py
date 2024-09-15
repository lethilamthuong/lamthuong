# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:24:47 2024

@author: Lenovo
"""
n=int(input("Nhập n:"))
S=0 
for i in range(1,n+1):
   S+=1/(i*(i+1))
print("S=1+1/n*(n+1)")