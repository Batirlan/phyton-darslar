#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 13:00:24 2021

@author: karzaubaevbatyrlangmail.com
"""

# Davlatlarning ro'yxatini tuzib, ro'yxatni konsolga chiqaramiz

davlatlar = ["Rossiya", "Kanada", "Germaniya", "Angliya", "Norvegiya"]
print(davlatlar)

# Ro'yxatning uzunligini konsolga chiqaramiz

print(f"Ruyxat ichida {len(davlatlar)} ta davlat nomi bor")

# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaramiz

print(sorted(davlatlar))

# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaramiz

print(sorted(davlatlar, reverse=True))

# Asl ro'yxatni qaytadan konsolga chiqaramiz

print(davlatlar)

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaramiz

davlatlar.reverse()
print(davlatlar)

# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, 
# keyin esa alifboga teskari tartibda konsolga chiqaramiz.

davlatlar.sort()
print(davlatlar)

davlatlar.sort(reverse=True)
print(davlatlar)

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzamiz.

juft_sonlar = list(range(120, 1200, 2))
print(juft_sonlar)

# Ro'yxatdagi sonlar yig'indisini hisoblab va konsolga chiqaramiz.

juft_sonlar = sum(juft_sonlar)

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblab 
# konsolga chiqaramiz.


print(max(juft_sonlar)-min(juft_sonlar))

# Ruyxatdagi elementlar nsonini xisoblaymiz

print(len(juft_sonlar))

# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring

print(juft_sonlar[:20])
print(juft_sonlar[-20:])
print(juft_sonlar[300:330])

# taomlar degan ro'yxat yarating va ichiga 5ta taomni kiritamiz

taomlar = ['manti', 'shashlik', 'osh', 'somsa', 'beshmarmak']


# nonushta degan yangi ro'yxatga taomlardan nusxa olamiz

nonushta = taomlar[:]


# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiramiz, 
# va qo'shimcha 2 ta taom qo'shamiz

nonushta.remove('manti')
nonushta.remove('beshmarmak')
nonushta.remove('shashlik')
nonushta.append('mastava')
nonushta.append('pelmen')

# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaramiz
print(taomlar)
print(nonushta)

# nonushta ruyxatini uzgarmas ruyxatga otkizamiz

nonushta = tuple(nonushta)
print(nonushta)

# Ruyxatga biror element qoshib koramiz

nonushta[0] = 'manti'
print(nonushta)





























