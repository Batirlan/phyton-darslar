#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 12:03:44 2021

@author: karzaubaevbatyrlangmail.com
"""

# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rab, 
# foydalanuvchi stop so'zini yozishi bilan dasturni to'xtatamiz.

savol = "Yaqshi korgan kitobingizni kiring: "
savol += "(Toxtatish uchin stop dep yozing!)"

while True:
    qiymat = input(savol)
    if qiymat == 'stop':
        break
print("Raxmat")

savol = "Yaqshi korgan kitobingizni kiring: "
savol += "(Toxtatish uchin stop dep yozing!)"
qiymat =''
while qiymat != 'stop':
    qiymat = input(savol)
    if qiymat != 'stop':
        print("Yana kiriting")

# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 
# 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 
# 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
# while tsikl yozamiz, dastur foydalanuvchi yoshini so'rasin
# va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit 
# deb yozganda dastur to'xtasin (ikkita shartni ham tekshiramiz).

savol = "Yoshingizni kiriting: "

while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(qiymat)
    
    if yosh<7:
        narx = 2000
    elif yosh<18:
        narx = 3000
    elif yosh<65:
        narx = 10000
    else:
        narx = 0
        
    if narx == 0:
        print("Sizga kirish bepul:")
    else:
        print(f"Sizga kirish narxi {narx} som:")
        


# Foydalanuvchi kiritgan sonni ildizini chiqaruvchi dastur

print("Kiritilgan sonning ildizini qaytaruvchi dastur:")
savol = "Musbat son kiriting:"
savol += "(Dasturni tugatish uchin exit dep yozing): "
ishora = True
while ishora == True:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} sonini ildizi {ildiz} ")
        

    
        
        
        
        
        
        
        
        
        
        
        
        
        
    

    
      
