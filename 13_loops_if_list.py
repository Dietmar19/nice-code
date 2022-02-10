"""
Define a Function called "temperature" mit one input
Define the following conditions
a) the temperature is higher than 30 degress
    then output "it is too warm"
b) the temperature is below 15 degrees
    then output "It is to cold"
output "It is pleasant"
possibiility of entering the temperature
Call the function with the entered value
"""
"""
def temperature(a):
    if a > 30:
        print("Es ist zu warm")
    elif a < 15:
        print("Es ist zu kalt")
    else:
        print("Die Temperatur ist angenehm")

b=eval(input("Gebe die Temperatur ein:   "))
temperature(b)  
"""
a = [1,3,4,8]
"""
b = a.pop(0) #return the deleted value
print(b)
"""
"""
del a[0] # return no value
print(a)
"""
"""
Create a tupel with integer values
Output on the console
Expand the tupel by two values
Output the first value in the first tupel
"""
"""
a = 1,2,5,8,9
print(a)
b = (6,7), a
print(b)
print(b[0][0])
"""
"""
create three variables called by current, highest and lowest temperature
Create an condition 
when the current temperature higher the lowest temperature and current temperature
lower the highest temperature
then output "the current temperature is between the highest and lowest temperature"
else "the current temperature is not between the highest and lowest temperature"
"""
"""
tempcurrent = 50.2
temphigh = 40.2
templow = -18.2
if tempcurrent < temphigh and tempcurrent > templow:
    print("The current temperature is between the highest and the lowest temperature")
else:
    print("The current temperature is not between the highest and the lowest temperature")
"""
supermarket = ["Rewe","Real","Penny", "Kaufland"]
count = 1
while count < 3:
    name = input("Insert the name of a supermarket:  ")
    if name in supermarket:
        print("Supermarket is found")
        count += 1
    else:
        print("Supermarket is not found")
        count += 1
    

