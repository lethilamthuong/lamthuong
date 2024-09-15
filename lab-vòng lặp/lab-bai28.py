# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:21:21 2024

@author: LeThiLamThuong-23722951
"""

while True:
    N = input("Nhập một số nguyên dương: ")
    if N.isdigit() and int(N) > 0:
        N = int(N)
        break
    else:
        print("Vui lòng nhập một số nguyên dương hợp lệ.")
print("Các ước số của", N, "là:")
for i in range(1, N + 1):
    if N % i == 0:
        print(i)