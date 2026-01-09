# Try Except Else and finally 
chai_order = {"masala" : 50, "ginger" : 40}

try : 
    chai_order["elaichi"]
except KeyError :
    print("The key you are trying to access doesnt exist!")

print("hello") 