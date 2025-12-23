# build an authorization decorator 
from functools import wraps

def auth(func) :
    @wraps(func)
    def wrapper(user_role) :
        if user_role != "admin" :
            print("access not granted!")
            return None
        else : 
            return func(user_role)
    return wrapper

@auth
def log(role) :
    print("access granted")

log("admin")