# tuples  immutable
spices_mix = ("ginger", "clove", "turmeric") #tuple (-)

print(f"{spices_mix}")

# unpack a tuple into seperate variables 
(spice1, spice2, spice3) = spices_mix
print(f"{spice1}, {spice2}, {spice3}")

# change values or switch values 
ginger_ratio , clove_Ratio = 2 , 1  #coz of tuple automatically it give value to them
print(f"{ginger_ratio}, {clove_Ratio}")

ginger_ratio, clove_Ratio = clove_Ratio, ginger_ratio # change value or switch values 
print(F"{ginger_ratio}, {clove_Ratio}")

# membership or check it includes or not

print(f"is cardamom include in mix spices ? {"cardamom" in spices_mix}")
print(f"is ginger include in mix spices ? {"ginger" in spices_mix}")
print(f"is Ginger include in mix spices ? {"Ginger" in spices_mix}") # false coz it also is case sensitive