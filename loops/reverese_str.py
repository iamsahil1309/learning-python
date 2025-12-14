# reverse a string using a loop 

input_str = input("enter the string value : ")
reverse_str = ""

for char in input_str :
    reverse_str = char + reverse_str 
print(f"{reverse_str}")