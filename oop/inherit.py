# inheritance and composition 
class BaseChai : 
    def __init__(self, type_):
        self.type = type_

    def prepare(self) :
        print(f"base {self.type}")

# inhertiance or inherit  and no constructor is made so python made one behind the scenes
class MasalaChai(BaseChai) :
    def add_spices(self) :
        print("add ginger, cardamam, elaichi")

# composition 
class ChaiShop :
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self) :
        print(f"{self.chai.type}")
        self.chai.prepare()

# inheritance and composition
class FancyChaiShop(ChaiShop) :
    chai_cls = MasalaChai

shop = ChaiShop()
fancy = FancyChaiShop()

shop.serve()
fancy.serve()
fancy.chai.add_spices()