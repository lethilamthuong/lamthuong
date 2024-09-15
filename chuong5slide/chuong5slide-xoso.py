# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:03:08 2024

@author: LeThiLamThuong-23722951
"""

import random
sove = int(input("Nhập số lượng vé số: "))
vesd = []
for i in range(sove):
    ve = []
    while len(ve) < 6:
        try:
            number = int(input("Nhập số thứ {} cho vé số {}: ".format(len(ve) + 1, i + 1)))
            if number < 1 or number > 45:
                print("Số phải nằm trong khoảng từ 1 đến 45.")
            elif number in ve:
                print("Số đã trùng. Vui lòng nhập số khác.")
            else:
                ve.append(number)
        except ValueError:
            print("Vui lòng nhập một số nguyên.")
    vesd.append(sorted(ve))
winning_numbers = sorted(random.sample(range(1, 46), 6))
giai = {3: 30000, 4: 300000, 5: 10000000, 6: 10000000000}
total_giai_money = 0
kqua_string = ""
for ve in vesd:
    match_count = len(set(ve) & set(winning_numbers))
    if match_count >= 3:
        giai_money = giai.get(match_count, 0)
        total_giai_money += giai_money
kqua_string += "Dãy số trúng thưởng là: "
for number in winning_numbers:
    kqua_string += str(number) + " "
kqua_string += "\nTổng số tiền thưởng nhận được là: " + str(total_giai_money) + " đồng"
print(kqua_string)