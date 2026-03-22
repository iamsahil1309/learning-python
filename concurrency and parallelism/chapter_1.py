import threading
import time

def order_tea():
    for i in range(1,4):
        print(f"taking order for #{i}")
        time.sleep(1)

def brew_tea():
    for i in range(1,4):
        print(f"brewing chai for #{i}")
        time.sleep(2)

order_thread = threading.Thread(target=order_tea)
brew_thread = threading.Thread(target=brew_tea)

order_thread.start()
brew_thread.start()

order_thread.join()
brew_thread.join()

print("all arders taken and chai brewed")