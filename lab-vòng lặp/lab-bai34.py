# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:38:27 2024

@author: Lenovo
"""

while True:
    n_input = input("Nhập một số nguyên dương: ")
    if n_input.isdigit():
        n = int(n_input)
        if n > 0:
            break
        else:
            print("Vui lòng nhập số nguyên dương.")
    else:
        print("Vui lòng nhập số nguyên hợp lệ.")
snt = True
if n <= 1:
    snt = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            snt = False
            break
if snt:
    print(n, "là số nguyên tố.")
else:
    print(n, "không phải là số nguyên tố.")