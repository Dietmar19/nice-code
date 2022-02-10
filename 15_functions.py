"""
Create a funcion called "say_something" without parameters
loop body contains two print - functions 
Output "Good bye2 and "Bye bye"
call this function
After this call create a print - function 
hand over to this function the following string "Test" 
"""

def say_something():
    print("Good bye")
    print("Bye bye")
say_something()
print("Test")

"""
def tri_recursion(k):
  if k > 0:
    print(k)
    print(k-1)
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(2)
"""
"""
def greet(*names):
	i=0
	print('Hello ', end='')
	while len(names) > i:
		print(names[i], end=', ')
		i+=1

greet('Steve', 'Bill', 'Yash') 
#greet('Steve', 'Bill', 'Yash', 'Kapil', 'John', 'Amir') 


"""
"""
def f(x, y):
    z = 2 * (x + y)
    return z
print("Programm fängt an!")
a = 3
res1 = f(a, 2+a)
print("Ergebnis des Funktionsaufrufs: ", res1)
a = 4
b = 7
res2 = f(a, b)
print("Ergebnis des Funktionsaufrufs: ", res2)
"""
"""
def fak(zahl):
    if zahl < 0:
        return None
    ergebnis = 1
    for i in range(2, zahl + 1):
        ergebnis *= i
       # print(ergebnis)
    return ergebnis

while True:
    eingabe = int(input("Gebe eine Zahl ein:  "))
    ergebnis = fak(eingabe)
    if ergebnis is None:
        print("Fehler")
    else:
        print(ergebnis)
"""
"""
def summe(a,b, d=1, c=4):
    return a+b+c+d

print(summe(2,3, d=5, c=5))
print(summe(d=5, c=5, a=2, b=3))
"""
"""
def function(a,b,*weitere):  # weitere referenziert auf ein leeres Tupel
    print("Feste Parameter:  ", a,b)
    print("Weitere Parameter: ", weitere)
function(1,2, "Hello world", [1,2,3])
"""
"""
def summe(*parameter):
    a = 0
    for p in parameter:
        a += p
    return a

print(summe(1,2,3,4,5))
"""