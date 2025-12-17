# list comprehension 
drinks = [
    "Iced Coffee",
    "masala tea",
    "Iced Tea",
    "ginger tea",
    "Iced Latte",
    "Iced Mocha"
]

iced_coffee = [tea for tea in drinks if "Iced" in tea]

print(iced_coffee)