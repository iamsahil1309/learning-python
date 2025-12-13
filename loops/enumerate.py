# use enumerate to give numbers too to the item 
menu = ["green", 'black',"macha","lemon"]

for idx, item in enumerate(menu, start=1) :
    print(f"{idx} is {item}")