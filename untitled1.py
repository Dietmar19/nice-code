# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:30:50 2021

@author: Dietmar
"""

# 3. Programm
"""
Drittes Programm
Dietmar Baumann
"""
datensatz1=[1,2,3,8]
datensatz1.remove(8)
print(datensatz1)
datensatz1.reverse()
print(datensatz1)
datensatz2=max(datensatz1)
print(datensatz2)

datensatz3=float(datensatz1[1]+2)
print(datensatz3)

tupel1="Dietmar", 63, "männlich"
print(tupel1[1])

datensatz4={'name':'Dietmar','alter':'63','Größe':'1,63'}
print(datensatz4['alter']) #alter
print(datensatz4.values())


temp=eval(input("Temperatur eingeben:"))

if temp==20:
    print("Temperatur ist 20 Grad")
else:
    
    print("Temperatur ist nicht 20 Grad)")
    
temp1=1

temp2=eval(input("Wert eingeben"))
    
while temp1 <= temp2:
        print("Wert:",temp1)
        temp1=temp1+1


          