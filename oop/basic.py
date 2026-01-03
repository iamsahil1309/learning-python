class Car : 
    total_Car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model 
        Car.total_Car += 1

    def get_brand(self) :                            #encapsulation
        return self.__brand
    
    def fuel_type(self) :                            #polymorphism
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

# CLASS VARIABLES - Add a class variable to Car that keeps track o the number of cars created.
# show 2 coz second variable is count when use car.totalcar. And always use class name, here it is Car. Dont use object name.
print(Car.total_Car) 