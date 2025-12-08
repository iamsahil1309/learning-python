# DICTIONARY 
chai_order = dict(type = "masala chai", size = "medium", sugar = 1)
print(f"{chai_order}")

# empty dictionary 
chai_nature = {}
print(f"{chai_nature}")

# add 
chai_nature['base'] = "black tea"
chai_nature["liquid"] = "milk"
print(f"{chai_nature}") 

# delete 
del chai_nature['liquid']
print(f"{chai_nature}")

# intersection 
new_chai = chai_order | chai_nature
print(f"{new_chai}")

# get method used to get someothing without giving error 
customer_note = chai_order.get("liquid", "no liquid present")
print(f"{customer_note}")

# update 
extra_spices = {"turmeric" : "Crushed", "ginger" : "sliced"}

chai_nature.update(extra_spices)
print(f"{chai_nature}")

# remove last item only 
chai_order.popitem()
print(f"{chai_order}")