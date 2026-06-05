from dogclass import Dog

class PoliceDog(Dog):
    def __init__(self, rank, name="Nasher", breed="Alsation", energy=3): # This does not inherit the default values of Dog
        super(PoliceDog, self).__init__(name, breed, energy)
        self.rank = rank
    def arrest(self):
        print("Woof! You're nicked! Now give me a treat!")
    def clean(self):
        print("Wiping down my badge!")

