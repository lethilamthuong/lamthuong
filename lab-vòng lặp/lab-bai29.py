# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:29:04 2024

# @author: LeThiLamThuong-23722951
"""
while True:
    N = input("Nhập một số nguyên dương: ")
    if N.isdigit() and int(N) > 0:
        break
    else:
        print("Vui lòng nhập một số nguyên dương hợp lệ.")
tong = 0
for digit in N:
    tong += int(digit)
print("Tổng các chữ số của", N, "là:", tong)
