#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 17:08:00 2021

@author: karzaubaevbatyrlangmail.com
"""
# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi
# harfini katta harfga o'zgatiruvchi funksiya yozamiz.


def bosh_harif(matnlar):
    """Ruyxatdagi matnlarning birinchi harfini,
    katta harfga ozgarturuvchi funksiya"""
    for n in range(len(matnlar)):
        matnlar[n]=matnlar[n].title()

ismlar = ['batir', 'polat', 'timur', 'arman', 'madi']
bosh_harif(ismlar)
print(ismlar)

# Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi 
# ro'yxat qaytaradigan qilib o'zgartiramiz.

def bosh_harf0(matnlar):
    """Ruyxatdagi matnlarning birinchi harfini,
    katta harfga ozgarturuvchi funksiya"""
    matnlar = matnlar[:]
    for n in range(len(matnlar)):
        matnlar[n]=matnlar[n].title()
    return matnlar

ismlar = ['batir', 'polat', 'timur', 'arman', 'madi']
katta_harf = bosh_harf0(ismlar)
print(katta_harf)

# Bahola funksiyani asl ro'yxatga o'zgartirish kiritmasdan faqat 
# lug'at qaytaradigan qilib yozamiz.

def bahola(ismlar):
    baholar = {}
    while ismlar:
        for ism in ismlar:
            baho = input(f"Talaba {ism.title()}ni baholan: ")
            baholar[ism] = baho
        return baholar

talabalar = ['arman', 'madi', 'timur', 'batir', 'erdawlet']
baholangan_talabalar = bahola(talabalar[:])
print(baholangan_talabalar)
        