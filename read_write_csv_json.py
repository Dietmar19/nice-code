

import csv
import json

summary_countries = {}

with open("C:\\Users\\Dietmar\\OneDrive\\Documents\\Repository Python\\nice-code\\staaten.csv", "r", encoding="utf-8") as file:
    
    rows = csv.reader(file, delimiter = ";") # Reader wird mitgegeben wie die Struktur deer Datei ist
    header = next(rows)

    for row in rows:
        entry = {
            header[0] : row[0],
            header[1] : row[1]
        }
     
 
      #  countries = row[0] + " " + row[1] --> auch möglich
        countries = f"{row[0]} {row[1]}"
       
        summary_countries[countries]  = entry
print(json.dumps(summary_countries, indent=4, ensure_ascii=False))   # ensure_ascii= False ent das des escaping von Html


with open("C:\\Users\\Dietmar\\OneDrive\\Documents\\Repository Python\\nice-code\\staaten_write.csv", "w", encoding="utf-8", newline="") as file_write: # newline ="" dadurch kein Zeilenumbruch
    writer = csv.writer(file_write, delimiter = ";")
    writer.writerow(header)

    columns = []
    for entry in summary_countries.values():
      column = []
      column.append(entry[header[0]])
      column.append(entry[header[1]])
      columns.append(column)
    writer.writerows(columns)
    # writer.writerow(column) auch möglich aber nicht so performant, da jedesmal auf die Platte zugegriffen wir---> jede Zeile wird einzeln geschrieben
    # aber notwenig wenn es sehr viele Daten habe, weil der Aufbau einer kompletten Liste sehr viel Arbeitsspeicher raubt zum Aufbau

    



