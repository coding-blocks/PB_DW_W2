# -*- coding: utf-8 -*-
l=[]
s=int(input("ENTER NUMBER OF ELEMENTS IN LIST: "))
for i in range(s):
    x=int(input("ENTER AN ELEMENT: "))
    l.append(x)
print(l)
maximum=l[0]
for i in range(s):
    if l[i]>=maximum :
        maximum=l[i]
print("The maximum number in the list is:",maximum)
