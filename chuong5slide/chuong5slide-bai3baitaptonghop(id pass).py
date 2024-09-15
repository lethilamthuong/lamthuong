# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:44:04 2024

@author:  LeThiLamThuong-23722951
"""
import re
user_id = input("Nhập ID User: ")
password = input("Nhập Password: ")
kt_user_id = True
if len(user_id) < 6 or len(user_id) > 24:
    kt_user_id = False
else:
    for char in user_id:
        if char in " !@#$%^&*()-=+":
            kt_user_id = False
            break
    if ' ' in user_id:
        kt_user_id = False
kt_password = True
if len(password) < 6 or len(password) > 24:
    kt_password = False
else:
    has_lower = has_digit = has_upper = has_special = False
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char in "$#@":
            has_special = True
    if not (has_lower and has_digit and has_upper and has_special):
        kt_password = False
if kt_user_id and kt_password:
    print("Đăng nhập thành công.")
else:
    if not kt_user_id:
        print("ID User không hợp lệ.")
    if not kt_password:
        print("Password không hợp lệ.")