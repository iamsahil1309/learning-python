# loopthrough to list and customer names and their bill 

names = ["jihyo", "mina", "momo", "chaeyoung"]
bill = [25, 45, 65, 75]

# use zip 

for name, bill in zip(names, bill) :
    print(f"{name} paid {bill}")