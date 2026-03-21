class BaseChai :
    def __init__(self, type_):
        self.type = type_

    def prepare(self) :
        print(f"Preparing {self.type} chai...")

# inheritance
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding ginger, clove etc")

# composition
class ChaiShop:
    chai_cls =BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")  #creating object using BaseChai, so now can use every func or method that present in basechai.

    def serve(self):
        print(f"serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyShop(ChaiShop):
    chai_cls = MasalaChai


shop = ChaiShop()
shop.serve()
fancy = FancyShop()
fancy.chai.add_spices()