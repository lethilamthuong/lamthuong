# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:34:57 2024

@author: LeThiLamThuong-23722951
"""
thang = input("Nhập tháng (1-12): ")
nam = input("Nhập năm: ")
while True:
    if thang.isdigit() and nam.isdigit():
        if 1 <= thang <= 12 and nam > 0:
            break
        else:
            print("Vui lòng nhập tháng trong khoảng 1-12 và năm dương.")
    else:
        print("Vui lòng nhập tháng và năm là số nguyên hợp lệ.")
namnhuan = False
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    namnhuan = True
ngay = 31
if thang == 2:
    if namnhuan:
        ngay = 29
    else:
        ngay = 28
elif thang in [4, 6, 9, 11]:
    ngay = 30

print("Tháng", thang, "năm", nam, "có", ngay, "ngày.")