class Pet:
    happy = 50
    energy = 50
    food = 50
    sleeping = False
    
    sprites = [["MONTY-HAPPY.png", "MONTY-SAD.png", "MONTY-MAD.png", "MONTY-EXCITED.png", "MONTY-ASLEEP.png"], ["FRANKIE-HAPPY.png", "FRANKIE-SAD.png", "FRANKIE-MAD.png", "FRANKIE-EXCITED.png", "FRANKIE-ASLEEP.png"]]
    
    def __init__(self):
        self.name = ""
        self.type = -1
        
    def setName(self, name):
        self.name = name
    
    def setType(self, type):
        self.type = type
    
    def decHappy(self, decBy):
        if self.happy > 0:
            if self.happy - decBy >= 0:
                self.happy -= decBy
            elif self.happy > 0:
                self.happy = 0
    
    def decEnergy(self, decBy):
        if self.energy > 0:
            if self.energy - decBy >= 0:
                self.energy -= decBy
            elif self.energy > 0:
                self.nergy = 0
    
    def decFood(self, decBy):
        if self.food > 0:
            if self.food - decBy >= 0:
                self.food -= decBy
            elif self.food > 0:
                self.food = 0
    
    def incHappy(self, incBy):
        if self.happy < 50:
            if self.happy + incBy <= 50:
                self.happy += incBy
            elif self.happy < 50:
                self.happy = 50
    
    def incEnergy(self, incBy):
        if self.energy < 50:
            if self.energy + incBy <= 50:
                self.energy += incBy
            elif self.energy < 50:
                self.energy = 50
            
    def incFood(self, incBy):
        if self.food < 50:
            if self.food + incBy <= 50:
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
            return 0
        elif self.energy < 20 & sleepVal == 1:
            self.sleeping = True
            energy = 50
            return 1

        elif sleepVal == 1:
            self.decHappy(5)
            return -1
    
    def wakeUp(self):
        self.sleeping = False
    
    def play(self, winVal):
        if self.sleeping:
            print("Your pet is sleeping")
        elif winVal < 1:
            self.decHappy(5)
        elif winVal > 0:
            self.incHappy(5)

            
    def status(self):
        if self.happy + self.food + self.energy < 80:
            min_val = min([self.happy, self.food, self.energy])
            if min_val == self.happy:
                return 0
            elif min_val == self.food:
                return 1
            else:
                return 2
        else:
            return 3

    def nap(self):
        self.incEnergy(15)

