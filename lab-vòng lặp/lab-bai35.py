# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:52:50 2024

@author: LeThiLamThuong-23722951

"""

n=int(input("Nhập số n:"))
S=sum(range(1,n+1,1))
if n>0:
        print("Tổng các số nguyên S=1+2+..+n là:",S)
else:
        print("Không hợp lệ")