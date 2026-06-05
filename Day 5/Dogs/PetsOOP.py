from dogclass import Dog

print(help(Dog))

dog1 = Dog("Kim", "Snoodle Terrier", 3)
dog2 = Dog("Churchill", "British Bulldog", 1)
dog3 = Dog("Doug", "Snouser Terrier", 2)
dog4 = Dog()
dog5 = Dog("Clifford", "Labrador")

dog1.setEnergy(5)
dog1.run()
dog1.run()
dog1.run()
dog1.run()
print()

for n in range(4):
    dog1.run()
    dog2.run()
    dog3.run()
    dog4.run()
    dog5.run()
    print()

dog1.eatAndSleep()
dog2.eatAndSleep()
dog3.eatAndSleep()
dog4.eatAndSleep()
dog5.eatAndSleep()
print()

print(dog1.getEnergy)
print()

dog1.bark()
dog2.bark()
dog3.bark()
dog4.bark()
dog5.bark()
print()

for n in range(4):
    dog1.run()
    dog2.run()
    dog3.run()
    dog4.run()
    dog5.run()
    print()

dog1.eatAndSleep()
dog2.eatAndSleep()
dog3.eatAndSleep()
dog4.eatAndSleep()
dog5.eatAndSleep()
print()

print(getattr(dog1, "energy"))
print(hasattr(dog1, 'energy'))
setattr(dog4, 'name', 'Clifford')
dog4.bark()