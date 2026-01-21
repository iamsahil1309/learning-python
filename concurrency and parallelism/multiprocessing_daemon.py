import multiprocessing
import time

def background():
    while True:
        print("Running...")
        time.sleep(1)

if __name__ == "__main__":
    p = multiprocessing.Process(target=background, daemon=True)
    p.start()

    time.sleep(3)
    print("Main program ends")
