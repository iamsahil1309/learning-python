recipes = {
    "breakfast": ["Omelette", "Sandwich", "Pancakes", "Poha", "Upma"],
    "lunch": ["Sandwich", "Veg Pulao", "Paneer Butter Masala", "Dal Tadka", "Chapati"],
    "dinner": ["Paneer Butter Masala", "Chapati", "Vegetable Stir Fry", "Sandwich", "Spaghetti Pasta"],
    "snacks": ["Sandwich", "French Fries", "Pakora", "Spring Rolls", "Pancakes"],
    "quick_meals": ["Sandwich", "Omelette", "French Fries", "Spaghetti Pasta"]
}

unique_set = {spice for ingridients in recipes.values() for spice in ingridients}

print(unique_set)