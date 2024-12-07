# Write a Program to input a number and check whether number is odd or even 

number = int(input("Enter a Number "))
if number % 2 == 0:
    print(f"The {number} is even")
else:
    print(f"The {number} is odd")


# same but operator value different

number = int(input("Enter a Number "))
if number % 2 == 1:
    print(f"The {number} is odd")
else:
    print(f"The {number} is even")