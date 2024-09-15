# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:38:54 2024

@author: LeThiLamThuong-23722951
"""

import re
email_input = input("Nhập địa chỉ email: ")
mienhople = {"gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com", "icloud.com"}
if "@" in email_input:
    local_part, *domain_parts = email_input.rsplit("@", 1)
    domain = domain_parts[0] if domain_parts else ""
    if len(local_part) >= 6 and not re.search(r"[^\w\.-]", local_part) and domain in mienhople:
        print("Địa chỉ email hợp lệ.")
    else:
        print("Địa chỉ email không hợp lệ.")
else:
    print("Địa chỉ email không hợp lệ.")