# write a program to input three numbers and find the greatest number among three.

num1 = int(input("Enter first Number "))
num2 = int(input("Enter second Number "))
num3 = int(input("Enter third Number "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is greatest among three numbers")
elif num2 > num1 and num2 > num3:
        print(f"{num2} is greatest among three numbers")
else:
    print(f"{num3} is greatest among three numbers")
