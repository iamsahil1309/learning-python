class Car : 
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model 

    def get_brand(self) :
        return self.__brand
    
    def fuel_type(self) :
        return "Petrol or Diseal"

    def full_name(self) :
        return f"{self.__brand}, {self.model}"

my_car = Car("toyota", "corolla")
# print(my_car.brand)
# print(my_car.model)
print(my_car.full_name())

# INHERITANCE
class ElectricCar(Car) :
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, model)

    def fuel_type(self):
        return "ELectric Charge"

my_electric_car = ElectricCar("Tesla", "Xs", "85kwh")
print(my_electric_car.full_name())
# print(my_electric_car.brand)

# ENCAPSULATION - To private the attribute and can see when call by a method like getter
print(my_electric_car.get_brand())

# POLYMORPHISM - demonstrate polymorphism by defining a method fuel_type Car and Electric car classes, but with different behaviors. Same method name in different class but different functianlity.
print(my_car.fuel_type())
print(my_electric_car.fuel_type())