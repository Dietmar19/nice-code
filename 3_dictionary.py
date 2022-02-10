"""
we need index at list
it would be better if we can use search term
we have keys ad values at dictionaries
"""

person1 = {"Name": "Klaus", "Age": 51, "Size": 1.76}
print(person1.keys())
print(person1.values())
print(person1.items()) #important for loops

print(person1["Name"])

del person1["Age"]
print(person1)

print(type("Klaus" in person1))

person1.clear()
print(person1)

person1.setdefault("Name" , "Jasmin") # add a key-value-couple
print(person1)
person1.update({"Name": "Jasminchen", "Age": 41}) # update the value for the key "Name"
print(person1)