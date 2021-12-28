"""
author: Dietmar
Date: 21.12.2021
"""

"""
dic= {"Name": "Baumann", "Vorname" : "Dietmar", "Age": 63, "Größe": 1.86}
print(dic["Age"])
"""
import os
from types import CodeType



country_dict = {}
filename = "C:\\Users\\Dietmar\\OneDrive\\Documents\\Repository Python\\nice-code\\Country.txt"
print(os.getcwd())
textfile = open(filename, "r")
   

for line in textfile:
    assign = line.split( ";")
    country_dict[assign[0]] = assign[1]
textfile.close()

value = 1
while value < 3:
   
    country = input("Geben sie bitte ein Land ein : ")
    
    if country in country_dict:
        print("Das deutsche Wort lautet: ", country_dict[country])
    else:
        print("Das Land kann leider nicht gefunden werden")  
        print(value)
    value+=1
       
        