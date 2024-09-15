# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:22:25 2024

@author: LeThiLamThuong-23722951
"""

dschiahetcho5 = []
for num in range(2018, 2829):
    if num % 2 == 0 and num % 5 == 0:
        dschiahetcho5.append(num)
print("Danh sách các số chẵn chia hết cho 5 từ 2018 đến 2828:")
for number in dschiahetcho5:
    print(number)