# print the multiplication table for a given number upto ten but skip the fifth iteration 

number = int(input("enter the number : "))

for i in range(1, 11) :
    if i == 5 :
        continue
    print(number, 'x', i, '=', number * i)