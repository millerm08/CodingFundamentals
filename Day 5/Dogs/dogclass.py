from abc import ABC, abstractmethod

class Dog(ABC):
    """
    This will be visible in the help function in PetsOOP.py
    """
    def __init__(self, name="Gromit", breed="Clay Terrier", energy=4):
        self.name = name
        self.breed = breed
        self.energy = energy
        self.maxEnergy = energy

    @abstractmethod
    def clean(self):
        pass

    def run(self):
        if self.energy > 0:
            print(f"{self.name} is running round the meadow!")
            self.energy -= 1
        else:
            print(f"{self.name} is all tuckered out!")

    def eatAndSleep(self):
        if self.energy == 0:
            print(f"{self.name} is eating and resting. *Much* *Munch* *Munch* zzz")
            self.energy = self.maxEnergy

    def bark(self):
        print("Woof! Woof!")
        print(f"{self.name} is barking at nothing again!")

    def setEnergy(self,amount):
        if amount >= self.maxEnergy:
            self.enrgy = self.maxEnergy
        elif amount < 0:
            self.energy = amount

    def getEnergy(self):
        return self.energy