# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:18:19 2024

@author: LeThiLamThuong-23722951
"""

n = int(input("Nhập một số nguyên dương n: "))
if n < 0:
    print("Số nhập vào không phải là số nguyên dương.")
else:
    giaithua = 1
    for i in range(1, n + 1):
        giaithua *= i
    print("Giai thừa của", n, "là:", giaithua)