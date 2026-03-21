class Chai :
    def __init__(self, type_, size):
        self.type = type_
        self.size= size

    def summary(self):
        return f"A {self.size}ml of {self.type} chai"
    

order = Chai("masala", 520)
print(order.summary())
        