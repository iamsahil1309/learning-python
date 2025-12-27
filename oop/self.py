# methods are just functions if they are created inside the class
class Chaicup : 
    size = 200

    def describe(self) :
        return f"A {self.size} ml of chai"
    
cup = Chaicup()
print(cup.describe())