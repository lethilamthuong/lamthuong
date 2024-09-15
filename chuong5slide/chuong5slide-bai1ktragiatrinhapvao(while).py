# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:08:16 2024

@author: LeThiLamThuong-23722951
"""
N = float(input("Nhập một giá trị trong khoảng [-99, 99]: "))
while True:
    if -99 <= N <= 99:
        break
    else:
        print("Giá trị không hợp lệ. Vui lòng nhập lại.")
print("Giá trị bạn đã nhập là:",N)