first_number = int(input("enter the first number: "))
second_number = int(input("enter the second number: "))
choice = input("enter your choice(add/sub/multiply/divide): ").lower()

match choice : 
    case "add" : 
        print(first_number + second_number)
    case "sub" : 
        print(first_number - second_number)
    case "multiply" :
        print(first_number * second_number)
    case "divide" :
        print(first_number / second_number)
    case _ :
        print(f"INVALID OPERATION")