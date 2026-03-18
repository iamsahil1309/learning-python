def add_gst(price,rate):
    return price * (100 + rate) / 100

orders = [100,150,500]

for order in orders:
    final_bill = add_gst(order,10)
    print(f"original : {order}, final : {final_bill}")