import pandas

d = pandas.read_csv("C:\\Users\\Dietmar\\OneDrive\\Documents\\Repository Python\\nice-code\\Orte.csv", delimiter=",")
print(d)
c = d.query("Region == 'Süd' & Bundesland == 'Bayern'")
print(c)