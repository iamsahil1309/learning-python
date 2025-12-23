# generators 

def serve_chai() :
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"

chai = serve_chai()

# print(chai)
for cup in chai :
    print(cup)

def chai_list() :
    yield "ginger"
    yield "elaichi"
    yield "green"

tea = chai_list()

print(next(tea))
print(next(tea))
print(next(tea))