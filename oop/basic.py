class Car : 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 

    def full_name(self) :
        return f"{self.brand}, {self.model}"

my_car = Car("toyota", "corolla")
# print(my_car.brand)
# print(my_car.model)
print(my_car.full_name())

# INHERITANCE
class ElectricCar(Car) :
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, model)

my_electric_car = ElectricCar("Tesla", "Xs", "85kwh")
print(my_electric_car.full_name())
print(my_electric_car.brand)