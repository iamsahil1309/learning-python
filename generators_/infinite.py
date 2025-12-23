# Infinite generators 

def infinite_gen() :
    count = 1
    while True :
        yield f"Rank : #{count}"
        count += 1

infinite = infinite_gen()

for _ in range(100) :                                       
    print(next(infinite))