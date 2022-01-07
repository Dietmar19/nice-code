import sys
class Player:
    def __init__(self, name, punkte=1000):
        self._name = name
        self._score = punkte

    def get_name(self):
        return self._name
    name = property(get_name)

    def get_score(self):
        return self._score

    def set_score(self, pkt):
        self._score=pkt
        if self._score <= 0:
            self._score = 0
            print("Game over")
    point = property(get_score, set_score)
player1 = Player("Dietmar", 10000)
print(player1.name)
player1.point=-100
print(player1.point)


