# Try Except Else and finally 
chai_order = {"masala" : 50, "ginger" : 40}

try : 
    chai_order["elaichi"]
except KeyError :
    print("The key you are trying to access doesnt exist!")

print("hello") 

def process_order(item, quantity) :
    try :
        price = {"masala" : 40}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError :
        print("Sorry that chai is not in the menu")
    except TypeError :
        print("Quantity must be in number")

process_order("ginger", 4)
process_order("masala", "two")     #operator overloading
process_order("masala", 4)