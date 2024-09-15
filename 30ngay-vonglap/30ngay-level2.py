# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:18:08 2024

@author: LeThiLamThuong-23722951
"""
#1
tong = 0
for i in range(101):
    tong += i 
print("Tổng tất cả các số từ 0 đến 100 là:", tong)

#2
tongchan = 0
tongle = 0

for i in range(101):
    if i % 2 == 0:
        tongchan += i
    else:
        tongle += i
print("Tổng tất cả các số chẵn từ 0 đến 100 là:",tongchan)
print("Tổng tất cả các số lẻ từ 0 đến 100 là:",tongle)