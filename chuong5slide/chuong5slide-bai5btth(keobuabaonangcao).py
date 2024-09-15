# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:54:07 2024

@author: LeThiLamThuong-23722951
"""

import random
options = ["Kéo", "Búa", "Bao"]
songuoi = random.randint(8, 20)
ketqua_string = ""
for i in range(songuoi):
    user_choice = input("Người {}: Nhập Kéo, Búa, hoặc Bao: ".format(i + 1)).strip()
    while user_choice not in options:
        user_choice = input("Lựa chọn không hợp lệ. Người {}, nhập lại Kéo, Búa, hoặc Bao: ".format(i + 1)).strip()
    machine_choice = random.choice(options)
    if user_choice == machine_choice:
        ketqua = "Hòa"
    else:
        win = (user_choice == "Kéo" and machine_choice == "Bao") or \
              (user_choice == "Búa" and machine_choice == "Kéo") or \
              (user_choice == "Bao" and machine_choice == "Búa")
        if win:
            ketqua = "Bạn thắng!"
        else:
            ketqua = "Máy thắng!"
    ketqua_string += "Người {} chọn: {}\n".format(i + 1, user_choice)
    ketqua_string += "Máy chọn: {}\n".format(machine_choice)
    ketqua_string += "Kết quả: {}\n\n".format(ketqua)
print(ketqua_string)