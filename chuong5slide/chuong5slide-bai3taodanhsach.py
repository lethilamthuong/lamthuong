# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:00:34 2024

@author: LeThiLamThuong-23722951
"""

import random
sophantu = random.randint(20, 30)
squares_list = []
for _ in range(sophantu):
    random_number = random.uniform(18, 99)
    square_gtbp = random_number ** 2
    squares_list.append(square_gtbp)
print("Số lượng các phần tử trong danh sách:", sophantu)
print("Danh sách các giá trị bình phương:")
for gtbp in squares_list:
    print(gtbp)