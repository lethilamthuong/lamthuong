# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:16:56 2024

@author: Lenovo
"""

n=int(input("Nhập giá trị n:")) 
if n>0 :
  S=0
  for i in range(1,n+1):
      S += i**2 
  print("Tổng bình phương các số nguyên đến n là:",S )