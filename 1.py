class Brick:
    def __init__(self, strength):
        self.strength = strength

    def getStrength(self):
        return self.strength

class Lizard:

    def __init__(self, speed, mass, size):
        self.speed = speed
        self.mass = mass
        self.size = size

    def breakBlock(self, brick):
        if self.speed*self.mass>brick.getStrength():
            speed = ((self.speed*self.mass) - brick.getStrength())/self.mass
            print("True")
        else:
            print("false")

myBrick = Brick(50)
print(myBrick.strength)

myLizard = Lizard(200, 300, 5)
print(myLizard.speed)

success = myLizard.breakBlock(myBrick)
print(success)