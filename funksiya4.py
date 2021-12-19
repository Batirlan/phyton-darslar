#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 17:52:01 2021

@author: karzaubaevbatyrlangmail.com
"""

# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozamiz.

def kopaytma(*sonlar):
    """Istalgancha sonlarni qabul qilib, 
    ularning ko'paytmasini qaytaruvchi funksiya"""
    yigindi = 1
    for son in sonlar:
        yigindi *= son
    return yigindi

print(kopaytma(5, 4 ,24, 35))

# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozamiz. 
# Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa 
# ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'ladi.

def talabalar_info(ism, familiya, **malumotlar):
    """Talabalar haqidagi ma'lumotlarini 
    lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar

talaba1 = talabalar_info('Batir', 'Karjaubaev', tyil=1997, tjoy='Muynak tumani')
talaba2 = talabalar_info("Madeniyet", 'Bisenbaev', tyil=1997, tjoy='Nukus tumani')
print(talaba1)
print(talaba2)
