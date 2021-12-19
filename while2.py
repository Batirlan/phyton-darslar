#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 13:20:34 2021

@author: karzaubaevbatyrlangmail.com
"""
# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozamiz. Mahsulotlar nomini
# birma-bir qabul qilib, yangi ro'yxatga joylaymiz.
 
 
savat = []
while True:
    buyrtma = input("Savatga maxsulot qoshing: ")
    savat.append(buyrtma)
    javob = input("Yana maxsulot qushasizmi? (ha/yoq) ")
    if javob == 'yoq':
        break

# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi 
# dastur yozamiz. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot 
# va uning narhi) kiritishni so'raymiz.

maxsulotlar = {}
ishora = True
while ishora:
    maxsulot = input("Maxsulot nomini kiriting: ")
    narxi = input("Narxini kiriting: ")
    maxsulotlar[maxsulot] = narxi
    javob = input("Yana maxsulot kiritasizmi? (ha/yoq) ")
    if javob != 'ha':
        ishora = False
        
# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi 
# ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan 
# solishitiramiz. Agar mahsuot e-bozorda mavjud bo'lsa mahuslot 
# narhini chiqaramiz, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'satamiz.

buyrtmalar = ['olma', 'piyoz', 'kartoshka', 'anor', 'uzum']
maxsulotlar = {'olma':5000,
                'anor':8000,
                'banan':10000,
                'piyoz':4000,
                'kapusta':3000
                }

while buyrtmalar:
    buyrtma = buyrtmalar.pop()
    if buyrtma in maxsulotlar.keys():
        narx = maxsulotlar[buyrtma]
        print(f"{buyrtma} narxi {narx} som.")
    else:
        print(f"Bizda {buyrtma} yoq!")
    
























    
