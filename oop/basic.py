# create a car class with attributes like brand and model then create instance of this class 
class Car : 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self) :
        return f"{self.brand} {self.model}"

class ElectricCar(Car) :
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        

# INHERITANCE
my_tesla = ElectricCar("Tesla","Model S", "85kwh")
print(my_tesla.brand) 
print(my_tesla.model) 
print(my_tesla.battery_size) 

print(my_tesla.full_name())  #can access the method or function present in its parent class
# my_car = Car("toyota","supra")
# print(my_car.brand)
# print(my_car.full_name())

