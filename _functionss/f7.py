# create a function that accepts any number of keyword arguments and prints them in the format key:value 
def kwarg_print(**kwargs) :
    for key , value in  kwargs.items() :
        print(f"{key} : {value}")

kwarg_print(name="goku")
kwarg_print(name = "vegeta", race = "saiyan")