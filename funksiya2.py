#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 15:40:22 2021

@author: karzaubaevbatyrlangmail.com
"""

# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
# email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida 
# qaytaruvchi funksiya yozamiz. Lug'atda foydalanuvchu yoshi ham bo'adi. 
# Ba'zi argumentlarni kiritishni ixtiyoriy qilamiz (masalan, tel.raqam, el.manzil)

def foydalanuvchi_info(ism, familiya, tyil, tjoy, email='', tel=''):
    """lugat kurinichida qaytaruvchi funksiya"""
    foydalanuvchi = {'ism' : ism,
                     'familiya' : familiya,
                     'tyil' : tyil,
                     'yosh' : 2021-tyil,
                     'tjoy' : tjoy,
                     'email' : email,
                     'tel' : tel
                     }
    return foydalanuvchi

# Yuqoridagi funksiyani while yordamida bir necha bor chaqiriamiz, 
# va foydalanuvchilar degan ro'yxatni shakllantiramiz. Ro'yxatdagi mijozlar
# haqidagi ma'lumotni konsolga chiqaramiz.

foydalanuvchilar = []
while True:
    print("Quyidagi malumotlarni kiriting:")
    ism = input("Ismingiz: ")
    familiya = input('Familiyangiz: ')
    tyil = int(input("Tugilgan yilingiz: "))
    tjoy = input("Tugilgan joyingiz: ")
    email = input("El. pochtangiz: ")
    tel = input("Tel. raqamingiz: ")
    foydalanuvchilar.append(foydalanuvchi_info(ism, familiya, tyil, tjoy, email, tel))
    javob = input("Yana qushasizmi? (ha/yoq)")
    if javob == 'yoq':
        break
print("Mijozlarimiz hqaida malumotlar:")
for foydalanuvchi in foydalanuvchilar:
    print(f"{foydalanuvchi['ism'].title()} {foydalanuvchi['familiya'].title()} "
          f"{foydalanuvchi['tyil']}-yilda {foydalanuvchi['tjoy'].title()} tumanida tugilgan. "
          f"yoshi {foydalanuvchi['yosh']} da, tel.raqami {foydalanuvchi['tel']} "
          f"el.manzili{foydalanuvchi['email']}")
    
    
# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozamiz

def kattasini_chiqar(x, y, z):
    """Uchta sonnan eng kattasini qaytaruvchi funksiya"""
    max = x
    if max<=y:
        max=y
    if max<=z:
        max=z
    return max

katta = kattasini_chiqar(11, 24, 6)
print(katta)

# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini,
# diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozamiz.

def aylana_info(radius, pi=3.14159):
    """aylaning radiusini qabul qilib olib, uning radiusini,
    diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya"""
    aylana = {'radius': radius,
              'diametr' : 2*radius,
              'perimetr' : 2*radius*pi,
              'aylana yuzi' : pi*radius**2
              }
    return aylana

radius = aylana_info(10)
print(radius)

        
    
    
    
    
    
    

















