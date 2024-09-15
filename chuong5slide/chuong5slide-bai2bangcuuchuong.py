# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:18:24 2024

@author: LeThiLamThuong-23722951
"""

for bcc in range(2, 10):
    print("Bảng cửu chương " + str(bcc) + ":")
    for i in range(1, 11):
        print(str(i) + " x " + str(bcc) + " = " + str(i * bcc))
    print()