# send values to generators 
# yield also paused untill get the value in yield

def chai_customer() :
    print("Welcome! What ou want to order?")
    order = yield
    while True : 
        print(f"Preparing : {order}")
        order = yield

stall = chai_customer()
next(stall) # start the generator here to line 4, line 5 wont execute coz didnt send any values

stall.send("Green tea")
stall.send("black tea")
stall.send("masala tea")