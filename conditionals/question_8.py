# Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("enter your password : ")

password_length = len(password)

# print(password_length)

if password_length  < 6 :
    print("your password is Weak")
elif password_length <= 10 :
    print("your password is Medium")
elif password_length > 10 :
    print("your password is Strong")