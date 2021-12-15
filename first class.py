
"""
autor: Dietmar
Datum: 09.12.2021
"""


class Mensch:
    anzahl = 0
    gesamt_groesse = 0
    durchsch = 0
    def __init__(self,name,alter,größe):
        self.Name=name
        self.Alter=alter
        self.Größe=größe

        Mensch.gesamt_groesse+=größe
        Mensch.anzahl+=1
        Mensch.durchsch=Mensch.gesamt_groesse/Mensch.anzahl
    def __del__(self):
        Mensch.anzahl-=1
        Mensch.gesamt_groesse-=self.Größe
        Mensch.durchsch=Mensch.gesamt_groesse/Mensch.anzahl
    def grüßen(self):
        print("Mein Name ist: ", self.Name)
mensch1=Mensch("Dietmar",63,1.86)
mensch1.grüßen()
mensch2=Mensch("Dagmar",63,1.63)
mensch2.grüßen()
print("Es existieren jetzt: ", Mensch.anzahl," Menschen mit einer Durschnittsgröße von: ", round(Mensch.durchsch,2))

del mensch1
print("Es existieren jetzt nur noch: ", Mensch.anzahl," Menschen mit einer Durschnittsgröße von: ", round(Mensch.durchsch,2))

