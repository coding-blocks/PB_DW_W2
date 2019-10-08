# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 09:03:31 2019

@author: PRASHANT
"""
def facto(n):
    if n==1:
        return (1)
    else:
        return n*facto(n-1)
a=int(input("Enter the number you want to find the factorial of: "))
if a==0:
    x=1
else:
    x=facto(a)
print(x)
