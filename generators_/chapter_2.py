# infinite generator and send value to generator 

def chai_order():
    print("what would you like to order ?")
    order = yield
    while True :
        print(f"preparing {order}")
        order = yield

stall = chai_order()
next(stall)
stall.send("masala chai")