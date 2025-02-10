'''Kim is writing an object-oriented program for a four player board game. The board has 26 squares that players move around'''

'''Write, using pseudocode, the constructor method for the Player class.'''
class Player():

    def __init__(self, playerid):
        self.playerid = playerid
        self.boardPosition = 0
        self.money = 2000

'''Write, using pseudocode, the constructor method for the Animal class.'''
class Animal():

    def __init__(self, name, cost, l0, l1, l2, l3, imageLink, setSquare, owned):
        self.name = name
        self.currentLevel = 0
        self.cost = cost
        self.l0 = l0
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.imageLink = imageLink
        self.setSquare = setSquare
        self.owned = owned

Squirrel=Animal(name="sqrr24", cost=2000, l0=2, l1=3, l2=4, l3=5, imageLink="sqrr24.bmp", setSquare=6, owned= "free")

print(Squirrel.name)
print(Squirrel.cost)
print(Squirrel.l0)
print(Squirrel.l1)
print(Squirrel.l2)
print(Squirrel.l3)
print(Squirrel.imageLink)
print(Squirrel.setSquare)
print(Squirrel.owned)