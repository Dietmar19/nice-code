
class Tree:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("My name is ", self.name, "Tree")
class FruitTree(Tree):
    def speak(self):
        print("I'm a ",self.name, "Tree")
    def grow(self, length):
        print("I grow eavery year ", length, "centimeters")

x = Tree("Maple")
y = FruitTree("Apple")
y.speak()
a = 50
y.grow(80)
"""
print(x, type(x))
print(y, type(y))
print(isinstance(y,Tree))
print(isinstance(y,FruitTree))
print(isinstance(x, FruitTree))
y.speak()
"""

