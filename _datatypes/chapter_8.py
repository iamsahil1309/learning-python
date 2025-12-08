# SETS

essential_spices = {"cinnaman", "ginger", "clove"}
other_spices = {"ginger", "cardamam", "turmeric"}

# UNION - GIVE UNIQUE SET (no same included)
new_spices = essential_spices | other_spices
print(f"{new_spices}")

# INTERSECTION- give common
mix_spices = essential_spices & other_spices
print(f"{mix_spices}")

# DIFFERENCE 
diff_spices =  other_spices - essential_spices 
print(f"{diff_spices}")

# MEMBERSHIP TEST 
print(f"is clove present in essential spice ? : {'clove' in essential_spices}")