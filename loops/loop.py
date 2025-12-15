# print number 1 to 10 
for i in range(1, 11) :
    print(f"{i}")

# print all evan number between 1 to 15 
for i in range(1,51) :
    if i%2 == 0 :
        print(f"{i}")

# multiplication table of a  given number 
number = int(input("enter the number: "))
for i in range(1,11) :
    print(number, "x", i, "=", number*i)

# sum of numbers from 1 to n 
number = int(input("enter the number : "))
sum_num = 0

for i in range(1, number+1) :
    sum_num = sum_num + i

print(f"{sum_num}")

# print all the number in the list 
nums = [3, 7, 2, 9, 5]

for num in nums : 
    print(num)

# count how many digits are in a given number 
number = input("enter the number: ")
digit = 0

for num in number : 
    digit += len(num)

print(f"{digit}")

# Find the factorial of a number using a loop.
number = int(input("enter the number : "))
factorial_num = 1

for i in range(1, number+1) :
    factorial_num = factorial_num*i

print(f"{factorial_num}")

# Print all prime numbers between 1 and 100.
for num in range(2, 101) :
    is_prime = True
    for i in range(2, num) :
        if num % i == 0 :
            is_prime = False
            break
    if is_prime :
        print(num)


# reverse a number using loop 
string_given = input("enter the value : ")
reverse = ""

for char in string_given :
    reverse = char + reverse
print(f"{reverse}")


