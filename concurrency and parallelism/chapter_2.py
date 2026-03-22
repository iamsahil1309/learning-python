import threading
import time

def boli_milk():
    print("milk is boiling")
    time.sleep(2)
    print("milk is boild....")

def make_breakfast():
    print("preparing breakfast")
    time.sleep(3)
    print("breakfast prepared....")

start = time.time()

t1 = threading.Thread(target=boli_milk)
t2  = threading.Thread(target=make_breakfast)

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()

print(f"total time taken is {end - start:.2f}")