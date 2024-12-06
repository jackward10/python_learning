# 1. Write a program which takes radious as an input and calculate the area of the circle.

r = int(input("Enter a radius of the circle "))
area = (22/7) * r ** 2
print(area) 


# 2. Write a program to find the frequency of the input number in a list .
numbers = [5,2,3,5,3,2,3,3,1,4]
input_number = int(input("Enter a Number to check the frequency ")) 
frquency = numbers.count(input_number)
print(frquency) 
print(f'The frequency of {input_number} is {frquency}')