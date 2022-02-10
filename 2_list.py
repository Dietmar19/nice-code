"""
Repetition of last session
1. create a program header
2. create a variable for the age
4. Detection of data type
3. print-Function with following content: I'm : age old
4. create the input-function for the age
"""


list1 = ["Tobi","Ricke","Klaus","Jasmin"]
list1.remove("Ricke")
print(list1)
list1.pop(1) #knallt einen bestimmten ab
print(list1)
list1.insert(1,"Ricke")
print(list1)
list1[1] = "Henrike"
list1.insert(2,"Klaus")
print(list1)
print(len(list1))

list2 = [1,2,3,4]
print(list2)

list1 = list1 + list2
print(list1)

list1.append("All")
print(list1)

list5 = list1.extend(list2)
 
print(list5)

list2.reverse()
print(list2)

list3 = sum(list2)
list4 = min(list2)
print(list3,list4)

list6 = range(5,10)
print(list6)
print(type(list6))  # ist keine List
list6 = list(list6)
print(list6)
list6.clear()
print(list6)


