# Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order = input("what size you want to order : ")
extra_shot = True

if extra_shot : 
    coffee = order + " coffee with an extra shot of espresso"
else :
    coffee = order + "coffee"

print(f"your order is {coffee } ")