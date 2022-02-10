"""
Create a loop, which is valid until right integer value is inserted
The program will be aborted if one insert a not correct value for example a character
Create an input with a prompt where you have to insert a number
output where the base is the inserted value and the exponent is also the inserted value
Output a error message "Ups, my mistake"
"""
"""
while True:   # ausgewählte Ausnahmen
    try:
        a = abs(int(input("Insert a number: ")))
        b = a**a
        print("Die",a," te Potenz von: ", a , "ist : ", b)
        break
    except ValueError:    #also several errors are possible in a list
       # except(RunTimeError, TypeError, NameError)
        print("Ups, my mistake")
"""
"""
Testing Error Handling
"""

"""
x = -1
if x < 0:
    raise Exception("Only integer values are allowed")
"""
"""
x = "Hello"
if type(x) is not int:
    raise TypeError("Only integer values are allowed")
"""

for x in range(1, 11):
    #print(x)
    print(repr(x).rjust(2) , repr(x*x).rjust(4,"*"), end=" ")
    # Achte auf die Benutzung von 'end' in der vorherigen Zeile
    print(repr(x*x*x).rjust(4))

