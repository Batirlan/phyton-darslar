#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 20:13:24 2021

@author: karzaubaevbatyrlangmail.com
"""

# Foydalanuvchidan juft son kiritishni so'rayiz. Agar foydalanuvchi juft son kiritsa 
# "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaramiz.

juft_son = int(input("Juft son kiriting: "))
if juft_son%2:
    print("Bu son jift emas")
else:
    print("Raxmat!")
    
# Foydalanuvchi yoshini so'raymiz va muzeyga kirish uchun chipta narhini
# quyidagicha chiqaramiz:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

yosh = int(input("Yoshingiz nechida?"))
if yosh < 4 or yosh > 60:
    narxi = 0
elif yosh <= 18:
    narxi = 10000
elif yosh > 18:
    narxi = 20000
print(f"Sizga kirish {narxi} som!")

# Foydalanuvchidan ikita son kiritishni so'rab sonlarni solishtiramiz 
# va ularning teng yoki katta/kichikligi haqida xabarni chiqaramiz:
    
print("Ikkita son kiriting:")
b = int(input("Birinchi son: "))
i = int(input("Ikkinchi son: "))
if b == i:
    print(f"{b}={i}")
elif b > i:
    print(f"{b}>{i}")
else:
    print(f"{b}<{i}")

# mahsulotlar degan ro'yxat yaratamiz va kamida 10 ta turli mahsulotni kiritamiz. 
# Yangi, savat degan bo'sh ro'yxat yaratib foydalanuvchidan savatga kamida 
# 5 ta mahsulot kiritishni so'raymiz. Savatdagi elementlarni, mahsulotlar ro'yxati
# bilan solishtirib qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" 
# aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaramiz.

maxsulotlar = ['banan', 'olma', 'sabzi', 'piyoz', 'orik', 'mandarin', 'pomidor', 'tarvuz', 'qovun', 'apeltsin']
savat = []
print("5 ta maxsulot kiriting:")
for n in range(5):
    savat.append(input(f"{n+1}-maxsulot: "))
for buyrtma in savat:
    if buyrtma in maxsulotlar:
        print(f"Bizda {buyrtma} maxsuloti bor")
    else:
        print(f"Bizda {buyrtma} maxsuloti yoq")


# Yuqoridagi dasturni quyidagicha o'zgartiramiz: foydalanuvchidan 5 ta mahsulot 
# kiritishni so'raymiz. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yangi, 
# bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas 
# degan ro'yxatga qo'shamiz. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan
# barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi 
# mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaramiz.

maxsulotlar = ['banan', 'olma', 'sabzi', 'piyoz', 'orik', 'mandarin', 'pomidor', 'tarvuz', 'qovun', 'apeltsin']
savat = []
print("5 ta maxsulot kiriting:")
for n in range(5):
    savat.append(input(f"{n+1}-maxsulot: "))
bor_maxsulotlar = []
mavjud_emas = []
for buyrtma in savat:
    if buyrtma in maxsulotlar:
        bor_maxsulotlar.append(buyrtma)
    else:
        mavjud_emas.append(buyrtma)
if mavjud_emas:
    print(f"Siz soragan quyidagi maxsulotlar mavjud emas")
    for buyrtma in mavjud_emas:
        print(buyrtma)
else:
    print("Siz soragan barcha maxsulotlar dokonimizda bor!")

# foydalanuvchilar degan ro'yxat tuzib 5 ta login qo'shamiz. 
# Foydalanuvchidan yangi login tanlashni so'raymiz va foydalanuvchi kiritgan
# loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiramiz.
# Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" 
# aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaramiz.

foydalanuvchilar = ['eldor', 'batirlan', 'timur', 'nurik', 'arman']
login = input("Login kiriting: ")
if login.lower() in foydalanuvchilar:
    print("Bu login band! Boshqa login kiriting!")
else:
    print(f"Xush kelibsiz {login.title()}!")
    
# Foydalanuvchidan biror butun son kiritishni so'raymiz. Foydalanuvchi kiritgan 
# sonni 2 dan 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini 
# konsolga chiqaramiz.

butun_son = int(input("Butun son kiriting: "))
for n in range(2,11):
    if not (butun_son%n):
        print(f"{butun_son} soni {n} ga qoldiqsiz bo'linadi")





                
    























