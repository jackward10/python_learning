# map()
# map() is a buitl-in function that takes two parameters as an input. First parameter is function
# and second parameter is an iterable
# map() function changes every element in an iterable to some other form

nums = [1, 2, 3, 4, 5]
def increase_by_10(data):
    return data +10

def increase_by_power(a):
    return a ** 3


result = map(increase_by_10, nums)
print(nums)
print(list(result))

r = map(increase_by_power, nums)
print(list(r))

result = map(lambda x: x + 10,nums) # using lambda function
print(list(result))