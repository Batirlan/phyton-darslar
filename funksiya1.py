#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 14:12:30 2021

@author: karzaubaevbatyrlangmail.com
"""
# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozamiz.

def tyil_xisobla(ism, yosh, jyil = 2021):
    """ism va yosh sorab tugilgan yilni,
    xisoblovchi funksiya"""
    print(f"Xurmatli {ism.title()}! Siz {jyil-yosh}da tugilgansiz.")

tyil_xisobla('batir', 24)

ism = input("Ismingizni kiriting: ")
yosh = int(input('Yoshingiz nechida: '))
tyil_xisobla(ism, yosh)

# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozamiz.

def kvadrat_kub_chiqar(son):
    """sonni kvadrati va kubini konsolga chiqaruvchi funksiya"""
    print(f"{son} ning kvadrati {son**2} ga kubi {son**3} ga teng")
    
kvadrat_kub_chiqar(24)

# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozamiz.

def juftmi(son):
    """sonni juft yoki toqligini konsolga chiqaruvchi funksiya"""
    if son%2 == 0:
        print("Juft son")
    else:
        print("Toq son")

juftmi(4)

# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozamiz. 
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaramiz.

def kattami(x, y):
    """sonni kattasini konsolga chiqaruvcgi funksiya"""
    if x>y:
        print(x)
    elif x<y:
        print(f"{y}")
    else:
        print("Sonlar teng")

kattami(13, 112)

# Foydalanuvchidan x va n sonlarini olib, x ning n darajasini konsolga 
# chiqaruvchi funksiya yozamiz.

def darajasini_chiqar(x, n):
    """x ning n darajasini konsolga,
    chiqaruvchi funksiya"""
    print(f"{x} ning {n} darajasi {x**n} ga teng")
    
darajasini_chiqar(10, 5)


# Yuqoridagi funksiyada n uchun 2 standart qiymatini beramiz.


def darajasini_chiqar1(x, n=2):
    """x ning n darajasini konsolga,
    chiqaruvchi funksiya"""
    print(f"{x} ning {n} darajasi {x**n} ga teng")
    
darajasini_chiqar1(54)

# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga 
# qoldiqsiz bo'linishini tekshiruvchi funksiya yozamiz.

def qoldiqsiz(son):
    """sonni 2 dan 10 gacha bo'lgan sonlarga,
    qoldiqsiz bo'linishini tekshiruvchi funksiya"""
    for n in range(2, 11):
        if son%n == 0:
            print(f"{son} soni {n} songa qoldiqiz bolinadi: {son}/{n}={son/n}")

qoldiqsiz(80)




















