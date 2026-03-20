def my_decorator(func) :
    def wrapper():
        print("hello")
        func()
        print("world")
    return wrapper


@my_decorator
def greet():
    print("hello world")

greet()