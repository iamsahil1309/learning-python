# example of mutable
spice_mix = set()  

# initially empty
print(f"initial spice mix : {spice_mix}") 
print(f"initial spice mix : {id(spice_mix)}") 

# adding spices
spice_mix.add("ginger") 
spice_mix.add("turmeric") 
spice_mix.add("garlic")

# now can add so it mutaded spice_mix in memory 
print(f"initial spice mix : {spice_mix}")
print(f"initial spice mix : {id(spice_mix)}")
