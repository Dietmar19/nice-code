"""
Author: Dietmar
Date: 19.12.2021
"""
a=[1,2,2,23,3]
print(a)
b=a.index(3)
print(b)

c="Hello World"
print(len(c))

print(min(a))
print(max(a))

a.append(8)
a.extend([1,87,34])
print(max(a))
a.insert(0, 100)
print(a)
a.sort()
print(a)
d=a.sort(reverse=True)
print(d)
a.pop(-1)
print(a)
a.remove(2)
print(a)
print(a.extend([45,67,98,47,47]))

print(a.sort())
e=a.count(47)
print(e)
a[1]=1000
print(a)
a[1:3]=[444]
print(a)
a[1:5]=[111]
print(a)