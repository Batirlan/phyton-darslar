#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 11:45:03 2021

@author: karzaubaevbatyrlangmail.com
"""

# Ismlar degan ro'yxat yaratamiz va kamida 3 ta yaqin do'stlat ismini kiritamiz
# Ro'yxatdagi har bir do'stimizga qisqa xabar yozib konsolga chiqaramiz:
    
dostlar = ["alisher", "azamat", 'polat']
print(f"Salom {dostlar[2].title()} ishlaring yaqshimi")
print(f"{dostlar[0].title()} {dostlar[1].title()}ni kormadingmi")
print(dostlar[1].title() + " qachon choyxonaga boramiz")


# sonlar deb nomlangan ro'yxat yaratamiz va ichiga turli sonlarni yuklaymiz
# (musbat, manfiy, butun, o'nlik).

sonlar = [24, 56, 85, -23, 10.4, 48.7, -39]
print(sonlar)


# # Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajaramiz.
# # Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiramiz, ba'zilarini esa almashtiramiz.

sonlar[1] = sonlar[1]+sonlar[3]
sonlar[2] = 59.3
sonlar[5] = sonlar[5]+78
sonlar[6] = 87
del sonlar[0]
print(sonlar)

# t_shaxslar va z_shaxslar degan 2 ta ro'yxat yaratamiz va biriga tarixiy shaxslarning, 
# ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiritamiz.

t_shaxslar = ["Alisher Navoyi", "Imom Buxoriy", "Amir Temur"]
z_shaxslar = ['Bill Geyts', 'Ilon Mask', 'Worren Baffet']
print(f"{t_shaxslar} \n{z_shaxslar}")

# # Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), 
# # quyidagi ko'rinishda chiqaramiz:
# # Men tarixiy shaxslardan Amir Temur bilan, zamonamiz shaxslaridan esa
# # Ilon Mask bilan suxbatlashishni istar edim
    
print(f"Men tarixiy shaxslardan {t_shaxslar.pop(2)} bilan, zamonamiz shaxslaridan esa \
      {z_shaxslar.pop(1)} bilan suxbatlashishni istar edim")
      
# friends nomli bo'sh ro'yxat tuzamiz va unga .append() yordamida 5-6 ta 
# mehmonga chaqirmoqchi bo'lgan do'stlarimizni kiritamiz.

friends = []
friends.append('Madinet')
friends.append("Arman")
friends.append("Ramet")
friends.append("Timur")
friends.append("Erdawlet")
print(friends)

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni 
# .remove() metodi yordamida o'chrib tashlaymiz.

friends.remove("Arman")
friends.remove("Erdawlet")
friends.remove("Ramet")
print(friends)

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shamiz.

friends.insert(0, 'Adil')
friends.insert(2, "Qayrat")
friends.insert(1, "Xamit")
friends.insert(5, "Madet")
print(friends)

# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yaratib. .pop() va .append() 
# metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan
# sug'urib olib, mehmonlar ro'yxatiga qo'shamiz.

mexmonlar = []
mexmonlar.append(friends.pop(0))
mexmonlar.append(friends.pop(2))
mexmonlar.append(friends.pop(3))
print(mexmonlar)



















































