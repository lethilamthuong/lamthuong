# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:20:04 2024

@author: Lenovo
"""

n=int(input("Nhập số n:"))
N=1
if n>0: 
  for i in range(1,n+1):
    N*= i 
  print("tích các số từ 1 đến {n}= ",N)
else:
    print("Không hợp lệ")
