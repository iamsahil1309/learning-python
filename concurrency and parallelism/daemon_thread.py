import threading
import time

def background():
    while True:
        print("Running...")
        time.sleep(1)

t = threading.Thread(target=background, daemon=True )  #daemon = true means this is a background helper and will automatically stop when the main program ends
start = time.time()
t.start()

time.sleep(10)
print(f"total time:{time.time() - start:.2f}")
print("Main program ends")
