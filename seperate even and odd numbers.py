# -*- coding: utf-8 -*-
a=[]
n=int(input("ENTER NUMBER OF ELEMENTS IN LIST: "))
for i in range(n):
    b=int(input("ENTER AN ELEMENT: "))
    a.append(b)
print(a)
even=[]
odd=[]
for j in a :
    if j%2==0 :
        even.append(j)
    else :
        odd.append(j)
print("even numbers are: ",even)
print("odd numbers are: ",odd)


