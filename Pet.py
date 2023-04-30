class Pet:
    happy = 50
    energy = 50
    food = 50
    sleeping = True
    
    sprites = [["MONTY-HAPPY.png", "MONTY-SAD.png", "MONTY-MAD.png"], ["FRANKIE-HAPPY.png", "FRANKIE-SAD.png", "FRANKIE-MAD.png"]]
    
    def __init__(self):
        self.name = ""
        self.type = -1
        
    def setName(self, name):
        self.name = name
    
    def setType(self, type):
        self.type = type
    
    def decHappy(self, decBy):
        if self.happy > 0 & self.happy - decBy >= 0:
            self.happy -= decBy
        elif self.happy > 0:
            self.happy = 0
    
    def decEnergy(self, decBy):
        if self.energy > 0 & self.energy - decBy >= 0:
            self.energy -= decBy
        elif self.energy > 0:
            self.nergy = 0
    
    def decFood(self, decBy):
        if self.food > 0 & self.food - decBy >= 0:
            self.food -= decBy
        elif self.food > 0:
            self.food = 0
    
    def incHappy(self, incBy):
        if self.happy < 50 & self.happy + incBy <= 50:
            self.happy += incBy
        elif self.happy < 50:
            self.happy = 50
    
    def incEnergy(self, incBy):
        if self.energy < 50 & self.energy + incBy <= 50:
            self.energy += incBy
        elif self.energy < 50:
            self.energy = 50
            
    def incFood(self, incBy):
        if self.food < 50 & self.food + incBy <= 50:
            self.food += incBy
        elif self.food < 50:
            self.food = 50
    
    def feed(self, feedVal):
        if self.sleeping:
            print("Your pet is sleeping")
        elif feedVal == 1:
            self.incFood(5)
        else:
            self.decHappy(5)
    
    def putToSleep(self, sleepVal):
        if self.sleeping:
            print("Your pet is sleeping")
        elif self.energy < 20 & sleepVal == 1:
            self.sleeping = True
        elif sleepVal == 1:
            self.decHappy(5)
    
    def play(self, winVal):
        if self.sleeping:
            print("Your pet is sleeping")
        elif winVal < 1:
            self.decHappy(5)
        elif winVal > 0:
            self.incHappy(5)
    def nap(self):
        self.incEnergy(15)