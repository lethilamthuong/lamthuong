# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:19:49 2024

@author: Lenovo
"""

n=int(input("Nhập số n:"))
S=sum(range(2,n+1,2))
if n>0:
  print("Tổng 2+4+6+..+{n} =",S)
else:
  print("Không hợp lệ")