

file = open("staaten.csv")

content = file.read()

rows = content.split("/n")

table = []

for row in range(len(rows)):
    column = row.split(";")
    table.append(column)

