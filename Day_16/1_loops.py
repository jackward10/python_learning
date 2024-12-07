# loops are used to run the certain block of codes repeatdly
# These are used to reduce the manual effort and perform the task in automated way
# There are two types loops in python ; for loop and while loop

# for loop in differernt datatypes

vowels = ["a", "e", "i", "o", "o"]

for each in vowels:
    print(vowels)

# looping is similar in tuple , list and set 

# Now lets see looping in Dictionary Type
student = {"name": "Jon", "age": 25, "address": "KTM"}
print(student.keys())

for key in student.keys():
    print(key)

print(student.values())

for value in student.values():
    print(value)

print(student.items())

for key, value in student.items():
    print(key)
    print(value)


#range() function

# we can give three parameters in the range function ; range(start, end, step-size)

a = range(10) # range object
print(a) #range object
print(list(a)) # [0,1,2,3,4,5,6,7,8,9]

a = range(2, 10) #gives from 2 to 9
print(list(a)) # [2,3,4,5,6,7,8,9]

a = range(2, 10, 2) # [2,4,6,8]
print(list(a))

squared = []
for i in range (1, 13):
    squared.append(i**2)
print(squared)

squared = [i**2 for i in range(1, 13)] # List comprehension
print(squared)


########## enumerate() ###########
#enumerete() function can take 2 parameters, iterable and start_value

vowels = ["a", "e", "i", "o", "o"]
print(enumerate(vowels)) #enumerate object
print(list(enumerate(vowels)))

for index, value in enumerate(vowels):
    print(index)
    print(value)

for index, value in enumerate(vowels, start=5):
# Here index counting starts form 1
    print(index)
    print(value)