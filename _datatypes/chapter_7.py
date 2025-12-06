# lists 
ingridients  = [ "ginger", "clove", "tumeric"]

# add in a lists 
ingridients.append("garlic")
print(f"{ingridients}")

# add in a particular position 
ingridients.insert(2, "chocolate")
print(f"{ingridients}")

# how to add to lists 
old_marvel = ["spiderman","ironman", "hulk"]
new_marvel = ["black panther", "daredevil", "bucky"]

old_marvel.extend(new_marvel)
print(f"{old_marvel}")

# remove from last 
old_marvel.pop()
print(f"{old_marvel}")

# reverse a list 
old_marvel.reverse()
print(f"{old_marvel}")

#sort 
old_marvel.sort()
print(f"{old_marvel}")

# min and max in lists 
sugar_level = [1,34,54,34,23,46,3]
print(f"max sugar level : {max(sugar_level)}")
print(f"min sugar level : {min(sugar_level)}")