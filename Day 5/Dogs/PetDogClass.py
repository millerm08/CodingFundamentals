from dogclass import Dog

class PetDog(Dog):
    def __init__(self, toys=33, name="Nintendog", breed="Poodle", energy=3):
        super(PetDog, self).__init__(name, breed, energy)
        self.toys = toys

    def play(self):
        print("Throw the ball! Throw it! Throw it! Throw it!")

    def clean(self):
        print("Just licking my balls")