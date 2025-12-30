class Car :
    def __init__(self, __brand, model):
        self.__brand = __brand
        self.model = model 

    def full_name(self) :
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand

# Inheritance 
class ElectricCar(Car) :
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, model)

my_car = Car("Maruti", "Suzuki")
print(my_car.get_brand())  
print(my_car.model)  
print(my_car.full_name())  

my_electric_car = ElectricCar("Tesla", "Model S", "85kwh")
print(my_electric_car.get_brand())
print(my_electric_car.battery_size)
print(my_electric_car.full_name())