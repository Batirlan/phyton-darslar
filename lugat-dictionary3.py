#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 19:06:03 2021

@author: karzaubaevbatyrlangmail.com
"""

# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar 
# haqidagi ma'lumotlarni lug'at ko'rinishida saqlaymiz. Lug'atlarni
# bitta ro'yxatga joylaymiz, va har bir shaxs haqidagi ma'lumotni
# konsolga chiqaramiz.


buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
            'tyil':810,
            'vyil':870,
            'tjoy':'Buxoro'
            }

qodiriy = {'ism':'Abdulla Qodiriy',
            'tyil':1894,
            'vyil':1938,
            'tjoy':'Toshkent'
            }

vohidov = {'ism':'Erkin Vohidov',
            'tyil':1936,
            'vyil':2016,
            'tjoy':"Farg'ona"
            }

navoiy = {'ism':'Alisher Navoiy',
            'tyil':1441,
            'vyil':1501,
            'tjoy':"Xirot"
            }
buyuk_shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
for buyuk_shaxs in buyuk_shaxslar:
    print(f"{buyuk_shaxs['ism'].title()} "
          f"{buyuk_shaxs['tjoy']}da " 
          f"{buyuk_shaxs['tyil']}-yilda tugilib "
          f"{buyuk_shaxs['vyil']}-yilda vafot etkan")
    
# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini 
# ham qo'shamiz. For tsikli yordamida muallifning ismi va uning asarlarini 
# konsolga chiqaramiz.
    
buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
            'tyil':810,
            'vyil':870,
            'tjoy':'Buxoro',
            'asari':'Al-Jomi as-Sahih'
            }

qodiriy = {'ism':'Abdulla Qodiriy',
            'tyil':1894,
            'vyil':1938,
            'tjoy':'Toshkent',
            'asari':'Otkan kunlar'
            }

vohidov = {'ism':'Erkin Vohidov',
            'tyil':1936,
            'vyil':2016,
            'tjoy':"Farg'ona",
            'asari':'Xiyonat'
            }

navoiy = {'ism':'Alisher Navoiy',
            'tyil':1441,
            'vyil':1501,
            'tjoy':"Xirot",
            'asari':'Xamsa'
            }

buyuk_shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
for buyuk_sh in buyuk_shaxslar:
    print(f"{buyuk_sh['ism'].title()} "
          f"{buyuk_sh['asari']} asarini yozgan")


# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'raymiz. 
# ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida 
# lugatda saqlaymiz. Natijani konsolga chiqaramiz.

kinolar = {
    'Madeniyet':['Sher, yurak', 'Dragon'],
    'Arman':['Uyda yolgiz', 'Kapitan amerika'],
    'Timur':['Omadli yigtlar', 'Dengiz']}

for kalit, qiymat in kinolar.items():
    print(f"\n{kalit.title()}ning sevimli kinolari:")
    for kino in qiymat:
        print(kino)

# Davlatlar degan lug'at yaratamiz, lug'at ichida bir nechta davlatlar haqida 
# ma'lumotlarni lug'at ko'rinishida saqlab har bir davlat haqida ma'lumotni
# konsolga chiqaramiz.

davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "kanada":{'poytaxt':"ottava",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }
for davlat, malumot in davlatlar.items():
    if davlat.lower()=="aqsh":
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
        print(f"\n{davlat.title()} poytaxti {malumot['poytaxt'].title()}"
              f"\nYer maydoni: {malumot['maydon']}"
              f"\nAholisi soni: {malumot['aholi']}"
              f"\nPul birligi: {malumot['pul birligi']}")


# Yuqoridagi dasturga o'zgartirish kiritamiz: konsolga barcha davlatlarni emas, 
# foydalanuvchi so'ragan davlat haqida ma'lumot beramiz. Agar davlat
# lug'atinmizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan 
# xabarni chiqaramiz.


davlat = input('Davlat nomini kiriting: ').lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")












