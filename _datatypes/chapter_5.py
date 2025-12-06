# string slicing indexing and encode and decode 

# normal string 
chai_type = "normal"
print(f"{chai_type}")

# indexing
chai_nature = "Aromatic and Bold"
print(f"{chai_nature[0:8]}") #last digit not included so in order to print aromatic, use 8
print(f"{chai_nature[:8]}")
print(f"{chai_nature[8:]}")
print(f"{chai_nature[::-1]}") #reverse a string


# encode and decode a string or special character 
label_text = "hello wórld"
encoded_text = label_text.encode("utf-8")
print(f"{encoded_text}")
decode_text = encoded_text.decode("utf-8")
print(f"{decode_text}")