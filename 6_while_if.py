"""while True:
    number = int(input("Gebe bitte eine Zahl ein"))
    result = 1
    while number > 0:
        result = result * number
        number = number -1
    
    print("Das Ergebnis ist: ", str(result))
"""
"""
while True:
    number = int(input("Geben Sie eine Zahl ein"))
    if number < 0:
        print("negative Zahlen sind nicht erlaubt")
        continue
    result = 1
    while number > 0:
        result = result * number
        number = number -1
    print("Ergebnis: ", str(result))
"""
"""
for a in ("Tobi", "Rike"):
    print(a)

for a in range(10,0,-2):
    print(a)
"""
while True:
    number = int(input("Gebe eine Zahl ein:  "))
    if number < 0:
        print("Keine Negative Zahlen bitte")
        continue
    result = 1
    for i in range(2, number + 1):
        result = result *i
    print("Das Ergebnis ist: ", str(result))





