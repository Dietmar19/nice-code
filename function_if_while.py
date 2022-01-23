# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 18:09:01 2021

@author: Dietmar
"""

def xsquare(x):
    y=x**5
    print("Die dritte Potenz von X :  ", y)
    
    
x=eval(input("Bitte eien Wert für x eingeben:  "))

xsquare(x)

def test1(x,y):
    z=x*y
    print("Das Produkt aus ", x, " und ", y, " ist = ", z)
    
r = eval(input("Gebe bite Wert1 ein: "))
s = eval(input("Gebe bite Wert1 ein: "))
test1(r,s)  


def temperature(a):
    if a > 30:
        print("Es ist zu warm")
    elif a < 15:
        print("Es ist zu kalt")
    else:
        print("Die Temperatur ist angenehm")

b=eval(input("Gebe die Temperatur ein:   "))
temperature(b)  

def test2(c):
    d=c**3
    return d 

c=eval(input("Gebe bitte einen Wert ein:  "))
f=test2(c)
e=c*f
print("Das Produkt aus ", c, "und ", f, "ist ", e)
"""
i=1
k=eval(input("gebe Wert ein:  "))
while i<=k:
    print("Wert:", i)
    i=i+1"""