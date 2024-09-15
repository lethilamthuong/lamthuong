# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:25:58 2024

@author: LeThiLamThuong-23722951
"""

dssochan = []
for num in range(2020, 3839):
    if num % 2 == 0:
        dssochan.append(num)
chiahet9 = []
for number in dssochan:
    if number % 9 == 0:
        chiahet9.append(number)
print("Danh sách các số chia hết cho 9:")
output = ""
for number in chiahet9:
    output += str(number) + "\t"
output = output.rstrip("\t")
print(output)