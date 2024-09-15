# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:17:45 2024

@author: LeThiLamThuong-23722951
"""

print("Sử dụng vòng lặp for:")
for i in range(11):  
    print(i)
#1    
for i in range(11):
    print(i)
    i = 0
while i <= 10:
    print(i)
    i += 1
#2
for i in range(10, -1, -1):
    print(i)
i = 10
while i >= 0:
    print(i)
    i -= 1
#3
size = 8
for _ in range(size):
    print('#' * size)
#4
for i in range(10):
    print(str(i) + " x " + str(i) + " = " + str(i * i))
#5
for i in range(101): 
    if i % 2 == 0:
        print(i)
#6
for i in range(101):
    if i % 2 != 0:
        print(i)