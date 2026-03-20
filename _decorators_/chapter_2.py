from functools import wraps

def locate_chai(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"caling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"brewing{func.__name__} complete")
        return result
    return wrapper

@locate_chai
def brewing(type):
    print(f"brewing {type} chai")

brewing("masala chai")
