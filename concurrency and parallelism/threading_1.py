import threading
import time

def take_orders():
    for i in range(1,4):
        print(f"taking order for #{i}")
        time.sleep(2)

def brew_chai():
    for i in range(1,4):
        print(f"brewing chai for #{i}")
        time.sleep(4)

# creating threads also example of multi threading
# doing multiple task at once
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

# start the threading
order_thread.start()
brew_thread.start()

# wait for both to finish then join
order_thread.join()
brew_thread.join()

print("all task done")