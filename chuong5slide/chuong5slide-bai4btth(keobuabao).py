# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:50:23 2024

@author: LeThiLamThuong-23722951
"""

import random
options = ["éo", "Búa", "Bao"]
user_choice = input("Nhập Kéo, Búa, hoặc Bao: ").strip()
while user_choice not in options:
    user_choice = input("Lựa chọn không hợp lệ. Nhập lại Kéo, Búa, hoặc Bao: ").strip()
machine_choice = random.choice(options)
print("Máy chọn:", machine_choice)
if user_choice == machine_choice:
    print("Hòa")
else:
    win = (user_choice == "Kéo" and machine_choice == "Bao") or \
          (user_choice == "Búa" and machine_choice == "Kéo") or \
          (user_choice == "Bao" and machine_choice == "Búa")
    if win:
        print("Bạn thắng!")
    else:
        print("Máy thắng!")