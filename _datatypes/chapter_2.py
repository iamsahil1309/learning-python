# example of mutable
spice_mix = set()

print(f"initial spice mix : {spice_mix}")
print(f"initial spice mix : {id(spice_mix)}") 

spice_mix.add("ginger") 
spice_mix.add("turmeric") 
spice_mix.add("garlic")

print(f"initial spice mix : {spice_mix}")
print(f"initial spice mix : {id(spice_mix)}")
