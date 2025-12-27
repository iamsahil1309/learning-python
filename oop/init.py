class ChaiOrder : 
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self) :
        return f"A {self.size} ml of {self.type} chai."
    
order = ChaiOrder("masala", 1000)
print(order.summary())