#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 12:10:39 2021

@author: karzaubaevbatyrlangmail.com
"""

# Quyidagi o'zgaruvchilarni yaratamiz:
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"

# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaramiz:
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati

kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
print(f"{kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")
# f-stringsiz chiqarish
print(kocha + " kochasi, " + mahalla + " mahallasi, " + \
      tuman + " tumani, " + viloyat + " viloyati")

    
# # Endi shularni foydalanuvchidan soraymiz

print("Quyidagilarni toldirib bizga yashash joyingiz haqida malumot bering")
kocha = input("Kochangfiz")
mahalla = input("Mahallangiz")
tuman = input("Tumaningiz")
viloyat = input("Viloyatingiz")
print(f"{kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozamiz
print(kocha + " kochasi, \n" + mahalla + " mahallasi, \n" + \
      tuman + " tumani, \n" + viloyat + " viloyati")

# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga 
# yuklab manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() 
# metodlarini qo'llab ko'ramiz.
    
manzil = f"{kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil.title())
print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())


