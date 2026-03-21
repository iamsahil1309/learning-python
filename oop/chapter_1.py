class Chaicup:
    size = 150

    def describe(self):
        return f"A {self.size}ml of cup"
    
chai = Chaicup()
print(chai.size)
print(chai.describe())

chai_two = Chaicup()
chai_two.size = 100
print(chai_two.size)