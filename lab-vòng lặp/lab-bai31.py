# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:41:49 2024

@author: LeThiLamThuong-23722951
"""
a_str= input("Nhập cạnh a: ")
b_str= input("Nhập cạnh b: ")
c_str= input("Nhập cạnh c: ")
while True:
    if a_str.isdigit() and b_str.isdigit() and c_str.isdigit():
        a =int(a_str)
        b =int(b_str)
        c =int(c_str)
        if a > 0 and b > 0 and c > 0:
            break
        else:
            print("Vui lòng nhập ba số nguyên dương.")
    else:
        print("Vui lòng nhập các số nguyên hợp lệ.")
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        loai = "Tam giác đều"
    elif a == b or b == c or a == c:
        sides = sorted([a, b, c])
        if sides[0]**2 + sides[1]**2 == sides[2]**2:
            loai = "Tam giác vuông cân"
        else:
            loai = "Tam giác cân"
    else:
        sides = sorted([a, b, c])
        if sides[0]**2 + sides[1]**2 == sides[2]**2:
           loai = "Tam giác vuông"
        else:
            loai = "Tam giác thường"
else:
    loai = "Không thể tạo thành tam giác"
print("Kết quả:",loai)