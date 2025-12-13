# continue and break 
flavor = ["ginger", "out of stock", "lemon", "discontinued","tulsi"]

for flavor in flavor :
    if flavor == "out of stock" :
        continue
    if  flavor == "discontinued" :
        break
    else :
        print(f"{flavor}")

