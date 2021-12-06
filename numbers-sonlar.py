#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 12:44:24 2021

@author: karzaubaevbatyrlangmail.com
"""

# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur yozamiz

son = int(input("Istalgan son kiriting"))
print(f"{son} ning kvadrati {son**2} ga, kubi {son**3} ga teng")

# Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, 
# konsolga chiqaruvchi dastur

yosh = int(input("Yoshingiz nechida\n>>> "))
t_yil = 2021 - yosh
print("Siz,", t_yil, "yili tugilgan ekansiz")

# Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi,
# ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur

print("Ikkita son kiriting:")
a = int(input("Birinchi son: "))
b = int(input("Ikkinchi son: "))
print(f"{a}+{b}=", a+b)
print(f"{a}-{b}=", a-b)
print(f"{a}*{b}=", a*b)
print(f"{a}/{b}=", a/b)