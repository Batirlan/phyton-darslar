#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 17:13:05 2021

@author: karzaubaevbatyrlangmail.com
"""

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzamiz, va ro'yxatdagi 
# har bir ismga takrorlanuvchi xabar yozamiz

ismlar = ['Azamat', 'Arman', "Qasimjan", "Qiriqbay", "Polat"]
for ism in ismlar:
    print(f"Salom {ism} ertaga darsga borasanmi?")
    print("Men dosting Batirlan!")
    
    
# # Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod necha marta takrorlanganligi" 
# # xaqida xabar chiqaramiz
                         
print(f"Kod {len(ism)} marta takrorlandi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzamiz. Ro'yxatning 
# xar bir elementining kubini yangi qatordan konsolga chiqaramiz.

toq_sonlar = list(range(11, 101, 2))
for sonlar in toq_sonlar:
    print(f"{sonlar} kubi {sonlar**3}")
    
# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rab, 
# kinolar degan ro'yxatga saqlab olamiz. 

kinolar = []
print("Eng sevimli 5 ta kinolaringizni nommini kiriting:")
for x in range(5):
    kinolar.append(input(f"{x+1}-kinoni kiriting: "))
print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini 
# (suhbatlashganini) so'raymiz, va har bir suhbatlashgan odamning ismini 
# birma-bir so'rab ro'yxatga yozamiz. Ro'yxatni konsolga chiqaramiz.

suxbatdoshlar = []
son = int(input("Bugun nechta inson bilan suxbatlashdingiz? "))
print("Xar bir suxbatlashgan insoningiz nomini kiriting: ")
for n in range(son):
    suxbatdoshlar.append(input(f"{n+1}-ismni kiriting: "))
print(suxbatdoshlar)

















