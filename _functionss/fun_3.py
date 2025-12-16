def calculate_bill(orders, price_per_cup) :
    return orders * price_per_cup

my_bill = calculate_bill(4,15)
print(my_bill)
print("order bill is ", calculate_bill(5,5))