# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:12:57 2024

@author:  LeThiLamThuong-23722951
"""
while True:
    input_str = input("Nhập một số thực trong khoảng [-89.9, 88.8]: ")
    try:
        sothuc = float(input_str)
        if -89.9 <= sothuc <= 88.8:
            break
        else:
            print("Giá trị không hợp lệ. Vui lòng nhập lại.")
    except ValueError:
        print("Giá trị không phải là số thực. Vui lòng nhập lại.")
print("Giá trị bạn đã nhập là:",sothuc)