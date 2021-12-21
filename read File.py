"""
author: Dietmar
Date: 21.12.2021
"""
dic= {"Name": "Baumann", "Vorname" : "Dietmar", "Age": 63, "Größe": 1.86}
print(dic["Age"])

country_dict = {}
filename = "Country.txt"
with open(filename, "r") as file:
    print(file.read())
"""
for line in textfile:
    assign = line.split( "")
    country_dict[assign[0]] = assign[1]
textfile.close()

while True:
    country = input("Geben sie bitte ein Land ein : ")
    if country in country_dict:
        print("Das Land in Deutsch ist: ", country_dict[country])
    else:
        print("Das Land kann leider nicht gefunden werden")

        """