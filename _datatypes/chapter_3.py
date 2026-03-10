# encode, string

name = "sahil"
order = "coffee"

print(f"one {order} for {name}")

# slicing

full_name = "harry potter"
print(f"{full_name[0:5]}")
print(f"{full_name[:5]}")
print(f"{full_name[::-1]}")
print(f"{full_name[7:]}")

# encode and decode used for special characters 
greet = "hóla"
print(f"{greet} amigo")
encode_greet = greet.encode("utf-8")
print(f"{encode_greet} amigo")
decode_greet = encode_greet.decode("utf-8")
print(f"{decode_greet} amigos")