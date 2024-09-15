# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:35:38 2024

@author: LeThiLamThuong-23722951
"""

str_input = input("Nhập chuỗi: ")
length = len(str_input)
special_chars = "!@#$%^&*()-=+./"
special_count = 0
lowercase_count = 0
digit_count = 0
uppercase_count = 0
for char in str_input:
    if char in special_chars:
        special_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isupper():
        uppercase_count += 1
print("Độ dài chuỗi:", length)
print("Số lượng ký tự đặc biệt:", special_count)
print("Số lượng ký tự chữ cái từ a-z:", lowercase_count)
print("Số lượng ký tự chữ số từ 0-9:", digit_count)
print("Số lượng ký tự chữ cái từ A-Z:", uppercase_count)