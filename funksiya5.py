#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 18:20:17 2021

@author: karzaubaevbatyrlangmail.com
"""
# Berilgan sonni 10 kopaytiruvchi lambda funksiya yozamiz.

kopaytma = lambda x : x*10
print(kopaytma(24))

# Ikki son qabul qilib, ularni yigindisini qaytaruvcgi funksiya.

yigindi = lambda x, y : x+y
print(yigindi(14, 44))

# Random moduli ichidagi sample funksiyasi yordamoda 0 dan 1000 gacha bolgan sonlar
# oraligidagi tasodifiy 10 ta sonlar ruyxatini tuzamiz.

import random as r
sonlar = list(r.sample(range(1000), 10))
print(sonlar)

# random() va lambda funksiyasi yordamida sonlarning kvadratini xisoblaymiz.

sonlar1 = [24, 45, 75, 97, 12, 18, 22]

xisobla = list(map(lambda n : n**2, sonlar1))
print(xisobla)

# filter() va lambda funksiyakari yordamida tuyxatdan toq sonlarni ajratib olamiz.

toq_sonlar = list(filter(lambda n : n%2!=0, sonlar1))
print(toq_sonlar)

