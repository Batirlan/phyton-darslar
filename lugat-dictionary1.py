#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:26:25 2021

@author: karzaubaevbatyrlangmail.com
"""


# onam degan lug'at yaratib lug'atga shu
# inson haqida kamida 4 ta m'alumot kiritamiz (ismi, tu'gilgan yili, shahri, 
# manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaramiz:
# Onam Kurbanova Orazgul Muynak tumanida 1964-yilda tugilgan
    
    
onam = {'ism':'orazgul', 'familiya':'kurbanova', 't_yil':'1964', 't_yeri':'muynak tumani'}
print(f"Onam {onam['familiya'].title()} {onam['ism'].title()}\
      {onam['t_yeri'].capitalize()}da {onam['t_yil']}-yilda tugilgan")
      
      
      
      
# Oila a'zolarimiz sevimli taomlari lug'atini tuzamiz. Lug'atda kamida 5 ta
# ism-taom jufltigi boladi. Kamida uch kishining sevimli taomini konsolga chiqaramiz: 
# Batirning sevimli taomi osh

taom = {'batir':'osh', 'maral':'manti', 'polat':'shashlik', 'qasim':'norin', 'maftuna':'somsa'}
taom1 = taom['batir']
print(f"Batirning sevimli taomi {taom1}")

print("Polatming sevimli taomi", taom['polat'])
print(f"Qasimning sevimli taomi {taom['qasim']}")

# Python izohli lu'gati tuzamiz: Lug'atga shu kunga qadar o'rgangan 
# 10 ta so'z (atamani) kiritamiz (masalan integer, float, string, if, 
# else va hokazo) va har birining qisqacha tarjimasini yozamiz.

lugat = {'integer':'butun son', 'float':'onlik son', 'string':'matn',
         'vatiable':'ozgaruvchi', 'list':'ruyxat', 'tuple':'ozgarmas ruyxat',
         'if':'agar', 'else':'aks holda', 'elif':'aks xolda agar', 'dictionary':'lugat'
         }
kalit = input("Biror soz kiriting: ").lower()
print(lugat.get(kalit, "Bunday soz mavjud emas"))
    
    
# Yuqoridagi vazifani if-else yordamida qilamiz, va natijani ham foydalanuvchiga 
# tushunarli ko'rinishda chiqaramiz.

kalit = input("Biror soz kiriting: ").lower()
tarjima = lugat.get(kalit)
if tarjima == None:
    print("Bunday soz mavjud emas")
else:
    print(f"Siz soragan {kalit.title()} manosi {tarjima} deb tarjima qilinadi")

    
    
    
    
    
    
    
    
    
    
    
    

