# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 19:26:27 2021

@author: Dietmar
"""

datensatz=["Dietmar", 63, 1.86]

print("ich heiße",datensatz[0])
print("Ich bin",datensatz[1],"Jahre alt")
print("Ich bin", datensatz[2],"m groß")

datensatz1=[1,2,3,4,5,6,7]
print(datensatz1[-2])

datensatz2=["Dagmar", 63, 1.63]

print("ich heiße",datensatz[0])
print("Ich bin",datensatz[1],"Jahre alt")
print("Ich bin", datensatz[2],"m groß")

datensatz3 = datensatz + datensatz2
print(datensatz2)

datensatz4=[
           ["Dietmar", 63, 1.86], #erstes element
           ["Dagmar", 63, 1.63] #zweites element
           ]

print(datensatz3[1])

liste= range(10)
print("range element", liste)

liste1=list(liste)
print("list element", liste1)

liste2=range(2,5)
liste3=list(liste2)
print(liste3)

datensatz.append("Tanzen")

datensatz5=max(datensatz1)
datensatz.insert(0, 'König')
print(datensatz)

