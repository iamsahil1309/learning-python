# calculate the sum of even numbers till upto given n 

number = int(input("enter the number : "))
sum_even = 0

for i in range(1, number+1) :
    if i%2 ==0 :
        sum_even+=1
print(f"{sum_even}")

    

    