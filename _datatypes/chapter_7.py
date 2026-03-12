# for batch in range(1,5):
#     print(f"Preparing chai for batch #{batch}")


names = ["Aman", "Riya", "Karan", "Priya", "Rahul", "Sneha"]

for name in names:
    print(f"Order ready for {name}")

# ENUMERATE 

for idx, name in enumerate(names, start=1):
    print(f"roll no {idx} : {name}")