import pandas
import numpy
"""
d = pandas.read_csv("C:\\Users\\Dietmar\\OneDrive\\Documents\\Repository Python\\nice-code\\Orte.csv", delimiter=",")
print(d)
c = d.query("Region == 'Süd' & Bundesland == 'Bayern'")
print(c)


labels = ["a","b","c"]
my_list = [10,20,30]
arr = numpy.array([10,20,30])
dic= {"a":10, "b": 20, "c": 30}

a = pandas.Series(data=my_list, index=labels)
b = pandas.Series(dic)
sales_q1 = pandas.Series(data=[250,450,550,120], 
                        index=["Deutschland","Polen","Griechenland", "Frankreich"])
sales_q2 = pandas.Series(data=[250,350,250,150], 
                        index=["Deutschland","Polen","Griechenland", "Ungarn"])


print(sales_q1+sales_q2)
"""

columns = ["W","X","Y","Z"]
index = ["A","B","C","D","E"]

from numpy.random import randint

data = randint(-100, 100, (5,4))

df = pandas.DataFrame(data,index,columns)
df1=df["Z"]       # mit einer Spalte hat man ein Series - nur eine Klammer
df2 = df[["W","Z"]]  # wenn du zwei Spalten wählst, hast du ein DataFrame - jetzt zwei Klammern
# print(df2)
df["neu"] = df["W"] - df["Z"]
print(df)
df =df.drop("neu", axis=1) # axis = 1 --> Spalte axis=0 --> Zeile
print(df)
#df = df.loc["C"]  # Ausgabe Zeile
df = df.loc[["C","D"],["W","X"]]
print(df)
df = df.iloc[0:2]
#df = df.iloc["X"]  # Ausgabe Spalte
print(df)