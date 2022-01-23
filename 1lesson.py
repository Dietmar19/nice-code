# das ist ein Kommentar

"""
author: Dietmar Baumann
created: 22.01.2022
"""

print("Hello world\n")
print(5/7)

variable_tes1 = 4  # Buchstaben , Zahlen , Unterstriche --> es darf nicht miteiner Zahl begonnen werden
                   # int - ganzzahlger
variable_test2 = 3.14 # float - Fließkommawert kein Komma sondern einen Punkt verwenden
first_name= "Tobias"  # name der Variablen sollte seiner Funktion entsprechen
                      # String - Zeichenkette

print("firstname")
print(first_name)
print("Mein Name ist: " + first_name)
print("Mein Name ist: ", first_name)

surname = "Beckmann"
print("Mein Name ist",first_name,surname)

size = input("Gebe bitte dein Größe ein: ") # Wert wird als String gespeichert
print(size)
print(2*size)

size1 = eval(input("Gebe bitte dein Größe ein: ")) # Wert wird als String gespeichert
print(size1)
print(2*size1)

size2 = eval(input("Gebe bitte dein Größe ein: ")) # Wert wird als String gespeichert
print(size2)
print(round(size2/3.1455678,3))