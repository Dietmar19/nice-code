
class Tree:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("My name is ", self.name, "Tree")
class FruitTree(Tree):
    #def speak(self):
       # print("I'm a ",self.name, "Tree")
    def grow(self, length):                                         # 2. Teil
        print("I grow eavery year ", length, "centimeters")

x = Tree("Maple")                           # 2. Teil        
y = FruitTree("Apple")                       # 2. Teil
y.speak()                                    # 2. Teil
a = 50                                        # 2. Teil
y.grow(80)                                  # 2. Teil

print(x, type(x))
print(y, type(y))

print(isinstance(y, Tree))
print(isinstance(y, FruitTree))
print(isinstance(x, FruitTree))
y.speak()


