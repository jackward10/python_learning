# lambda in python are the elegant way to create a on-line functions
# These functions do not have name. so , they are also called as anonymous function

def addtion(a, b):
    return a + b

sum = lambda a, b : a + b
print(sum(4, 5))

is_even = lambda x: x % 2 == 0
print(is_even(4))

