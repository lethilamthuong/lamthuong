# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:16:44 2024

@author: LeThiLamThuong-23722951
"""
class NVVanPhong:
    pass
class NVBanHang:
    pass
nv_vp_data = [
    ("NVVP001", "Nguyen Van A", 5000000, 6000000, 20),
    ("NVVP002", "Tran Thi B", 5500000, 6500000, 22),
    ("NVVP003", "Le Thi C", 6000000, 7000000, 18),
    ("NVVP004", "Pham Van D", 5200000, 6200000, 25),
    ("NVVP005", "Hoang Thi E", 5800000, 6800000, 21)
]

nv_bh_data = [
    ("NVBH001", "Vu Thi F", 4000000, 5000000, 30),
    ("NVBH002", "Nguyen Thi G", 4200000, 5200000, 28),
    ("NVBH003", "Mai Van H", 4300000, 5300000, 32),
    ("NVBH004", "Dao Thi I", 4100000, 5100000, 25),
    ("NVBH005", "Bui Van J", 4400000, 5400000, 27)
]

nv_van_phong_list = []
for data in nv_vp_data:
    nv = NVVanPhong()
    nv.ma_nhan_vien = data[0]
    nv.ho_ten = data[1]
    nv.luong_co_ban = data[2]
    nv.luong_hang_thang = data[3]
    nv.so_ngay = data[4]
    nv_van_phong_list.append(nv)

nv_ban_hang_list = []
for data in nv_bh_data:
    nv = NVBanHang()
    nv.ma_nhan_vien = data[0]
    nv.ho_ten = data[1]
    nv.luong_co_ban = data[2]
    nv.luong_hang_thang = data[3]
    nv.so_san_pham = data[4]
    nv_ban_hang_list.append(nv)
    
print("Nhân viên văn phòng:")
for nv in nv_van_phong_list:
    print("Ma NV: {}, Ho Ten: {}, Luong Co Ban: {}, Luong Hang Thang: {}, So Ngay: {}".format(
        nv.ma_nhan_vien, nv.ho_ten, nv.luong_co_ban, nv.luong_hang_thang, nv.so_ngay))
print("Nhân viên bán hàng:")
for nv in nv_ban_hang_list:
    print("Ma NV: {}, Ho Ten: {}, Luong Co Ban: {}, Luong Hang Thang: {}, So San Pham: {}".format(
        nv.ma_nhan_vien, nv.ho_ten, nv.luong_co_ban, nv.luong_hang_thang, nv.so_san_pham))