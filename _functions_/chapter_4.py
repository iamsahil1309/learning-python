# comprehension list 

menu = [
    "masala chai",
    "iced tea",
    "iced mocha",
    "spicy tea",
    "no sugar tea",
    "iced americano"
]

iced_tea = [tea for tea in menu if len(tea) > 8]
print(iced_tea)