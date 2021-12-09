#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:24:44 2021

@author: karzaubaevbatyrlangmail.com
"""


# Python izohli lug'atini yaratamiz va lug'atga kamida 10 ta so'z qo'shamiz.
# Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo 
# ketma-ketligida chiroyli qilib konsolga chiqaramiz.

lugat_python = {'integer':'butun son', 'float':'onlik son', 'string':'matn',
          'vatiable':'ozgaruvchi', 'list':'ruyxat', 'tuple':'ozgarmas ruyxat',
          'if':'agar', 'else':'aks holda', 'elif':'aks xolda agar', 'dictionary':'lugat'
          }
for kalit, qiymat  in sorted(lugat_python.items()):
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat}")
    
# Davlatlar va ularning poytaxtlari lug'atini tuzamiz. Avval lug'atdagi davlatlarni, 
# keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaramiz.

davlatlar = {'Rossiya':'Moskva', 'Uzbekistan':'Tashkent',
             'karakalpakstan':'Nukus', 'Kazakstan':'Astana',
             'Germanya':'Berlin', 'Kanada':'Ottava'
             }
print("Men borgan davlatlar ruyxati:")
for davlat in sorted(davlatlar.keys()):
    print(davlat.title())
    
print("Yuqaridagi davlatlar poytaxtlari:")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())
    
# Foydalanuvchidan istalgan davlatni kiritishni so'raymiz va shu davlatning poytaxtini 
# konsolga chiqaramiz. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, 
# "Bizda bunday ma'lumot yo'q" degan xabarni chiqaramiz.

davlat0 = input("Istalgan davlat kiriting:")
davlat1 = davlatlar.get(davlat0)
if davlat1 == None:
    print("Keshirasiz bizda bu davlat togrisida malumot yoq")
else:
    print(f"{davlat0.upper()} poytaxti {davlat1.title()}")
    
# Restoran menusi lug'atini tuzamiz (kamida 10 ta taom-narh juftligini kiritamiz). 
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'raymiz. Foydalanuvchi kiritgan 
# taomlarni menu bilan solishtiramiz, agar taom menuda bo'lsa narhini ko'rsatamiz, 
# aks holda "bizda bunday taom yo'q" degan xabarni chiqaramiz.

menu = {'manti':15000, 'osh':12000, 'somsa':5000, 'shashlik':10000,
            'qazon kabob':30000, 'norin':14000, 'pelmen':11000,
            'tovuq':20000, 'beshmarmak':20000, 'pizza':18000}
mexmon = []
print('3 ta taom buyrtma qiling:')
for n in range(3):
    mexmon.append(input(f"{n+1}-taomni kiriting: "))
for buyrtma in mexmon:
    if buyrtma in menu:
        print(f"Bizda {buyrtma} bor narxi {menu[buyrtma]} som")
    else:
        print(f"Bizda {buyrtma} yoq")
        
    
    
    
    
    
    
    
    
    
    
    
    
