#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 18:38:02 2021

@author: karzaubaevbatyrlangmail.com
"""

# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzib, 
# ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaramiz. GM uchun 
# ikkala harfni katta qilamiz.

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())
        
# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaramiz.

for car0 in cars:
    if car0 != 'gm':
        print(car0.title())
    else:
        print(car0.upper())
        
# Foydalanuvchi login ismini so'raymiz, agar login admin bo'lsa, 
# "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" 
# xabarini konsolga chiqaramiz. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" 
# matnini konsolga chiqaring.

ism = input("Login kiriting: ")
if ism.lower() == 'admin':
    print("Xush kellibsiz Admin. Foylanuvchi ruyxatini korasizmi?")
else:
    print(f"Xush kelibsiz {ism.title()}!")
    
# Foydalanuvchidan 2 ta son kiritishni so'rab, agar ikki son bir-biriga teng bo'lsa, 
# "Sonlar teng" ekan degan yozuvni konsolga chiqaramiz.

print("Ikkita son kiriting:")
n = int(input("Birinchi son: "))
z = int(input("Ikkinxci son: "))
if n == z:
    print(f"Sonlar teng ekan! {n}={z}")
    
# Foydalanuvchidan istalgan son kiritishni so'rab, agar son manfiy bo'lsa konsolga 
# "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaramiz.

son1 = int(input("Istalgan son kiriting; "))
print("Musbat son") if son1 > 0 else print("Manfiy son")  

    
# Foydalanuvchidan son kiritishni so'raymiz, agar son musbat bo'lsa uning 
# ildizini hisoblab konsolga chiqaramiz. Agar son manfiy bo'lsa, 
# "Musbat son kiriting" degan xabarni chiqaramiz.

son2 = float(input("Son kiriting: "))
if son2 > 0:
    print(son2**(1/2))
else:
    print("Musbat son kiriting")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    