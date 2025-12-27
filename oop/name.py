class Chai : 
    origin = "India"

print(Chai.origin)

# add properties 
Chai.is_hot = True
print(Chai.is_hot)    #now class chai has new property name is_hot

# create object from class chai 
masala = Chai()

# now masala can access all the properties that class chai has

print(masala.origin)
print(masala.is_hot)