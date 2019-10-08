# -*- coding: utf-8 -*-
"""
Created on Wed Oct 8 09:05:52 2019

@author: PRASHANT
"""

s=input("Enter a paragraph : ")
s=s.lower()
l=s.split()
d={}
for i in l:
    d[i]=d.get(i,0)+1
print(d)


