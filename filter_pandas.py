
import pandas
import numpy
"""
d = pandas.read_csv("C:\\Users\\Dietmar\\OneDrive\\Documents\\Repository Python\\nice-code\\Orte.csv", delimiter=",")
#print(d)

c = d.query('Region == "Sued"' or  'Bundesland == "Bayern",', inplace = True) 
print(c)
"""
"""
rows = ["a","b","c"]                #alle Fälle
col = ["col1", "col2","col3"]       #alle fälle
rows1 = ["a","b"]
my_list = [10,20,30]                # alle Fälle
my_list1 = [[1,2,3] ,[4,5,6]]  #5. Fall
arr = numpy.array([10,20,30])
dic= {"a":10, "b": 20, "c": 30}
print(rows)
print(my_list)
a = pandas.Series(my_list)         # 1. Fall   1. Wert ist der reale Wert
print(a)
a = pandas.Series(my_list, rows)  # 2. Fall 2. Wert ist die Spaltenbezeichnung
print(a)

a = pandas.DataFrame(my_list)  # 3.Fall macht aus einer eindimensionalen Liste eine Tabelle mit Zeilen und Spalten
print(a)
a = pandas.DataFrame(my_list,index=rows) # 4.Fall
print(a)

a = pandas.DataFrame(my_list1,index=rows1, columns=col)    # 5. Fall
print(a)
"""


sales_q1 = pandas.Series(data=[250,450,550,120], 
                        index=["Deutschland","Polen","Griechenland", "Frankreich"])
sales_q2 = pandas.Series(data=[250,350,250,150], 
                        index=["Deutschland","Polen","Griechenland", "Ungarn"])

print(sales_q1)
print(sales_q1+sales_q2)

#b = pandas.Series(dic)
#print(b)

"""
columns = ["W","X","Y","Z"]
index = ["A","B","C","D","E"]

from numpy.random import randint

data = randint(-100, 100, (5,4))  # 5 Zeilen, 4 Spalten

df = pandas.DataFrame(data,index,columns)
print(df)
df1=df["Z"]       # mit einer Spalte hat man ein Series - nur eine Klammer
df2 = df[["W","Z"]]  # wenn du zwei Spalten wählst, hast du ein DataFrame - jetzt zwei Klammern
print(df1)
print(df2)

df["neu"] = df["W"] - df["Z"]
print(df)
"""

#df =df.drop("neu", axis=1) # axis = 1 --> Spalte axis=0 --> Zeile
#print(df)
"""
#df = df.loc["C"]  # Ausgabe Zeile
df = df.loc[["C","D"],["W","X"]]
print(df)
df = df.iloc[0:2]
#df = df.iloc["X"]  # Ausgabe Spalte
print(df)
"""