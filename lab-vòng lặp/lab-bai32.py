# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:46:50 2024

@author: LeThiLamThuong-23722951
"""
while True:
    km_input = input("Nhập số km đi: ")
    if km_input.isdigit():
        km = int(km_input)
        if km >= 0:
            break
        else:
            print("Vui lòng nhập số km không âm.")
    else:
        print("Vui lòng nhập số km là số nguyên hợp lệ.")
tien = 0
if km > 0:
    tien += 15000
if km > 1:
    if km <= 5:
        tien += (km - 1) * 13500
    else:
        tien += 4 * 13500
if km > 5:
    tien += (km - 5) * 11000
if km > 120:
    tien *= 0.9
print("Tiền cước TAXI cho", km, "km là:", tien, "đồng.")