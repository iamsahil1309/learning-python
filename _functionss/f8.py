# write a generator function that yields even numbers upto specified limit 
def limiter(limit) :
    for i in range(2,limit + 1,2) :
        yield i 

for num in limiter(10) :
    print(num)