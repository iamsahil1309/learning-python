class BaseChai :
    def __init__(self, type_):
        self.type = type_

    def prepare (self) :
        print(f"{self.type}")

#INHERITANCE
class MasalaChai(BaseChai) :
    def add_spice(self) :
        print("ginger")

#COMPOSITION
class ChaiShop :
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self) :
        print(f"serving {self.chai.type} chai")
        self.chai.prepare()

class FancyShop(ChaiShop) :
    chai_cls = BaseChai

shop = ChaiShop()
fancy = FancyShop()

shop.serve()
fancy.serve()
# fancy.chai.add_spice()
fancy.chai.prepare()
fancy.serve()