# create a car class with attributes like brand and model then create instance of this class 
class Car : 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("toyota","supra")
print(my_car.brand)

