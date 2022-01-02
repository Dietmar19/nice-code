import json

json_daten = """
{
    "ID" : 1,
    "Vorname" : "Klaus",
    "Nachname" : "Mustermann",
    "Telefon" : {
        "Festnetz" : "+49 03454 647",
        "Mobil" : "+49 4545343888"
        }
}
"""

python_daten = json.loads(json_daten)
print(type(json_daten), json_daten)
print(type(python_daten), python_daten)
print(python_daten["Telefon"] ["Mobil"])
# Umwandlung Daten in Dictionary in Jin ein Json String umwandeln

json_dump = json.dumps(python_daten, indent=4)
print(type(json_dump), json_dump)

#Json aus Datei lesen

with open("C:\\Users\\Dietmar\\OneDrive\\Documents\\Repository Python\\nice-code\\daten.json", "r") as json_datei:
    print(type(json_datei))
    python_liste = json.load(json_datei)
    print(type(python_liste), python_liste)
    print(python_liste[2] ["Vorname"])


