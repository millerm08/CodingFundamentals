items = ["Apples", "Oranges", "Grapes"]

for i in range(len(items)):
    print(items[i], " \t- Select number", i+1)

print()

try:
    sel = int(input("Please enter your choice: "))
    print(f"You have chosen: {items[sel - 1]}.")
except IndexError:
    print("Invalid selection, you silly customer!")
except ValueError:
    print("Please use a whole number digit.")
except:
    print("Something went wrong.")
"""
if sel > 0 and sel <= len(items):
    print(f"You have chosen: {items[sel - 1]}.")
else:
    print("Invalid selection.")
"""
print("Thank you for shopping here.")