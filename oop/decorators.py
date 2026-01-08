# Timing function execution - write a decorator that measures the time a function takes to execute
import time

def timer(func) :
    def wrap(*args, **kwargs) :
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrap

@timer
def example_fun(n) :
    time.sleep(n)

example_fun(2)