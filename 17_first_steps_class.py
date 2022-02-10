
"""
Nutzen der OOP
Bisher hast du mit sehr einfachen Daten gearbeitet
Bsw. integer, float, strings, list
Wenn du dich umschaust siehst du Menschen, Autos, deine Möbel usw.
Diese Objekte kannst du nicht 
mit bisher gelernten Datentypen abbilden
Wir müssen uns also eigene Datentypen schaffen,
die das können
Spiel
Menschen Autos z.B bei einen Autorennspiel
dazu gehören aber auch Bäume
Ich benötige also eine Übersicht über alle Objekte, die im Programm agieren sollen
Für diese Objekte generiert man eigene Datentypen, die dann miteinander interagiereen 
Bsw du kennst schon die class int,..
warum nicht eine class mensch Auto anlegen das dessen Eigenschaften besitzt
Bauplan ein Klasse
"""
print(type(3))

"""
class Car:
    def __init__(self):    #wenn ein neues Objekt angelegt wird--> wird die init-Methode
                           # aufgerufen und diese Attribute - Objekte übergeben
                           # durch self werden diese Attribute nur der ents.yprechenden Instanz
                           #zugeordnet--> Verhinderung des Überschreibens durch eine andere Instanz
        self.car_brand = None
        self.horse_power = None
        self.color = None
        self.x_position = 5    #2. Part der Vorstellung
        self.y_position = 5    #2.Part der Vorstellung
    def drive(self,x,y):           #2.Part der Vorstellung
        self.x_position += x
        self.y_position += y

car1 = Car()
print(car1.x_position)
print(car1.y_position)

car1.drive(5,10)
print(car1.x_position)
print(car1.y_position)
"""
"""     
         car1 = Car()        # Speicherplatz reserviert--> sichtbar print(car1) Wert hinter objekt
                    # das bedeutet alle Objekte des Objektes car1 werden hier gespeichert
                    # Wert ist nur eine Referenz auf das Objekt(Anfangsadresse im Speicher)
print(car1.horse_power)
car1.car_brand = "Audi"
print(car1.car_brand)
car2 = Car()
print(car2.horse_power)
car2.car_brand = "VW"
print(car1.car_brand)
print(car1)
print(car2)
car3 = car1
#print(car3) # derselbe Speicherplatz

print(car2)
"""











