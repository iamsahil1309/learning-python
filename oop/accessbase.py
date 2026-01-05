#THREE WAYS TO ACCESS BASE CLASS
class Chai : 
    def __init__(self, type_ , strength):
        self.type = type_
        self.strength = strength

#CODE DUPLICATION
# class GingerChai(Chai) :
#     def __init__(self,type_, strength, spice_level) :
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level

#EXPLICIT CALL
class Gingerchai(Chai) :
    def __init__(self, type_, strength, spice_level) :
        Chai.__init__(self, type_, strength)
        self.spice_level = spice_level


#SUPER
class MintChai(Chai) :
    def __init__(self, type_, strength, spice_level):
        self.spice_level = spice_level
        super().__init__(type_, strength)