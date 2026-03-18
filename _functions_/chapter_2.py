def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

calculate_bill(2,5)
my_bill = calculate_bill(5,2)
print(f"{my_bill}")
print("order for 3 : ", calculate_bill(3 , 5))