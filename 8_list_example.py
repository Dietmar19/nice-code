"""
Erstelle eine Liste mit den Werten von 1 bis 5
Gebe diese Liste auf der Konsole aus
"""
a=[1,2,3,4,5]
print(a)
"""
Gebe bitte den Wert vom Listenplatz 3 dieser Liste auf der Konsole aus
"""
b=a.index(3)
print(b)
"""
Gebe bitte den maximalen und minimalen Wert dieser Liste auf der Konsole aus
"""
print(min(a))
print(max(a))
"""
Erweitere die Liste um den Wert 8
Gebe dann die erweiterte Liste auf der Konsole aus
Erweitere bitte die besthende Liste um eine weitere Liste mit den Wert 10,20,30
Gebe dann die erweiterte Liste auf der Konsole aus
"""
a.append(8)
print(a)
a.extend([10,20,30])
print(a)
"""
Füge bitte an die erste Stelle der Liste den Wert 2 ein
Gebe dann die erweiterte Liste auf der Konsole aus
Sortiere die Liste der Größe nach
Gebe die sortierte Liste auf der Konsole aus
Sortiere die Liste nach den kleinsten Wert
Gebe die sortierte Liste auf der Konsole aus
"""
a.insert(0, 2)
print(a)
a.sort()
print(a)
d=a.sort(reverse=True)
print(d)
"""
Entferne bitte den letzten Wert der Liste
Gebe bitte die aktuelle Liste auf der Konsole aus
"""
a.pop(-1)
print(a)
"""
Entferne den Wert 4 der Liste
Gebe bitte die aktuelle Liste auf der Konsole aus
"""
a.remove(4)
print(a)
"""
Ermittle bitte die Anzahl der Listenelemente welche den Wert 2
Gebe die Anzahl auf der Konsole aus
"""
e=a.count(2)
print(e)
"""
Ersetze den Wert auf dem Listenplatz 2 durch den Wert 1000
Gebe bitte die aktuelle Liste auf der Konsole aus
"""
a[1]=1000
print(a)
"""
Ersetzen die Werte vom Listenplatz 1 - 3 mit dem Wert 444
Gebe bitte die aktuelle Liste auf der Konsole aus
"""
a[1:3]=[444]
print(a)
"""
Erstelle eine Variable mit den Wert "Hallo World"
Gebe bitte die Länge dieses Strings auf der Konsole aus
"""
c="Hello World"  #blank wird mitgezählt
print(len(c))





