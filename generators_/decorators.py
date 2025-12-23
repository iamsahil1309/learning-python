# decorators 
from functools import wraps

# def my_decorator (func) :
    
#     def wrapper () :
#         print("hello, start")
#         func()
#         print("hello end")
#     return wrapper

# @my_decorator
# def greet() :
#     print("hello middle")

# greet()
# print(greet.__name__)   # here print wrapper i.e,meta date of greet change 

#to prevent meta data , use wraps from functools

def my_dec(func) :
    @wraps(func)
    def wrapper() :
        print("start")
        func()
        print("end")
    return wrapper

@my_dec
def greet() :
    print("middle")

greet()
print(greet.__name__)