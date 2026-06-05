from dogclass import Dog

class SnifferDog(Dog):
    def __init__(self, smell=50, name="Nosey", breed="Springer Spaniel", energy=6):
        super(SnifferDog, self).__init__(name, breed, energy)
        self.smell = smell

    def sniff(self):
        print(f"{self.name} is sniffing you out...")
    
    def clean(self):
        print(f"Booping my snoot clean!")