def add_vat(price, vat_rate) :
    return price * (100 + vat_rate)/100

orders = [100,150,200,250]

for order in orders :
    final_bill = add_vat(order, 10)
    print(f"original order : {order}, finall bill : {final_bill}")