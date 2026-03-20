# def chai_list() :
#     return ["cup1", "cup2", "cup3"]

# chai = chai_list()
# print(chai)

def chai_gen() :
    yield "cup1"
    yield "cup2"
    yield "cup3"

chai = chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
print(next(chai))
print(next(chai))