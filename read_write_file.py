

file = open("C:\\Users\\Dietmar\\OneDrive\\Documents\\Repository Python\\nice-codes\\staaten.csv")

content = file.read()

rows = content.split("/n")

table = []

for row in range(len(rows)):
    column = row.split(";")
    table.append(column)

