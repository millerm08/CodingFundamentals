from dogclass import Dog

class RescueDog(Dog):
    def __init__(self, job="Mountain Rescue", name="Terry", breed="Staffie", energy=6):
        super(RescueDog, self).__init__(name, breed, energy)
        self.job = job

    def M_Rescue(self):
        print(f"{self.name} is on the scene")
        print(f"{self.name} will guide you off the mountain.")

    def clean(self):
        print("Shaking myself down!")