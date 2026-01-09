class InvalidChaiError(Exception) : pass

def bill(flavor, cups) :
    menu = {"masala" : 20, "ginger": 30}
    try : 
        if flavor not in menu : 
            raise InvalidChaiError("that chai is not available")
        if not isinstance(cups, int) :
            raise TypeError("Number of cups must b an integer")
        total = menu[flavor] * cups
        print(f"The bill for {cups} cups of {flavor} chai : rupee {total}")
    except Exception as e:
        print("Error", e)
    finally : 
        print("thank You!!") 


        
bill("mint", 2)
bill("masala", "three")
bill("ginger", 3)
