recipes = {
    "masala chai" : ["ginger", "cardamom", "clove"],
    "elaichi chai" : ["cardamom", "milk"],
    "spicy chai" : ["ginger", "black pepper", "clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)