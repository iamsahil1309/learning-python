# Movies tickets are priced based on age:$12 for adults(18 or above), $8 for children. Everyone gets a $2 discount on wednesday.
age = int(input("enter your age : "))
day = 'Wednesday'

price = 12 if age >=18 else 8

if day == "Wednesday" : 
    price -= 2

    print(f"your ticket price is ${price}")