cakes = int(input("How many cakes? "))
people = int(input("How many people? "))

try:
    print(f"There will be {cakes/people} cakes per person.")
except ZeroDivisionError:
    print("Sad party and lots of wasted cake!")
except:
    print("Something went wrong.")
else:
    print("Nothing went wrong.")
finally:
    print("That was an attempt at cake calculation.")
print("Thank you for using CalcACake.")