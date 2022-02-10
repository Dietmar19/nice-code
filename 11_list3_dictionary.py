# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:39:24 2021

@author: Dietmar
"""
"""
list1=[1,2,3]
list1.append(5)
print(list1)
list1.remove(1)
print(list1)

a=min(list1)
print(a)

b=list1[2]
print(b)
list1.insert(0,13)
print(list1)
"""
"""
# import untitled3
b=eval(input("Gebe wert ein: "))
c=test2(b)
print(c)
"""
"""
d={'Name':'Dietmar Baumann','Familienstand' :'verheiratet'}
print(d.items())
d.update({'Beruf': 'Informatiker'})
print(d)
d.pop('Familienstand')
print(d)
"""
obst=['Apfel','Birne','Pflaume']
obstsuche = input('Gebe Obstorte ein   ')

for n in obst:
    if n == obstsuche:
        print('obst vorrätig')
        break
print('Obst nicht vorrätig')