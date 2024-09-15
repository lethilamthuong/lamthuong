# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 04:16:47 2024

@author: LeThiLamThuong-23722951
"""

n = input("Nhập một số nguyên dương n: ")

# Kiểm tra và chuyển đổi giá trị của n
while True:
    if n.isdigit():
        n = int(n)
        if n > 0:
            break
        else:
            print("Số nguyên phải lớn hơn 0. Vui lòng nhập lại:")
    else:
        print("Vui lòng nhập một số nguyên hợp lệ:")
    n = input()

# In mô hình bàn cờ n x n
for i in range(n+3):
    row = ""
    for j in range(n+3):
        row += "  "
    print(row.strip())