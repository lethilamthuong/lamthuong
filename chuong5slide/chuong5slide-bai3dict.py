# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:32:14 2024

@author: LeThiLamThuong-23722951
"""

n = int(input("Nhập giá trị nguyên n: "))
ds = {}
for i in range(1, n + 1):
    ds[i] = i ** i
print("Dictionary vừa tạo là:")
print(ds)