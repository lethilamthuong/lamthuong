# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:50:26 2024

@author: LeThiLamThuong-23722951
"""

import math
while True:
    n_str = input("Nhập một số nguyên dương: ")
    if n_str.isdigit():
        n = int(n_str)
        if n > 0:
            break
        else:
            print("Vui lòng nhập số nguyên dương.")
    else:
        print("Vui lòng nhập số nguyên hợp lệ.")
sqrt_n = math.isqrt(n)
if sqrt_n * sqrt_n == n:
    print("Số", n, "là số chính phương.")
else:
    print("Số", n, "không phải là số chính phương.")