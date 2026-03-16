# walrus operator 
flavors = ["lemon", "ginger", "spicy", "sweet"]

while (flavor := input("enter your flavor : ")) not in flavors:
    print(f"{flavor} is not available")
print(f"your got {flavor} flavor")

