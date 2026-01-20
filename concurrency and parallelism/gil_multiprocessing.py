from multiprocessing import Process
import time

def brew_chai():
    print("Started brewing chai...")
    # here overwriting or bypassing the mutext
    count = 0
    for _ in range(100_00_000):
        count+=1
    print("Finished brewing chai...")

if __name__ == "__main__" :
    start = time.time()

    p1 = Process(target=brew_chai)
    p2 = Process(target=brew_chai)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()
    
    print(f"total time taken is {end - start:.2f} seconds")