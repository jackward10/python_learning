# *args and **kwargs are the arbitrary arguments 
# These arguments can take dynamic number of parameters
# They are like an expandable bucket

# *args (argument)
def addition(*args):
    # print(args)
    # print(sum(args))
    # print(type(args)) # tuple
    return sum(args)

addition(1,2,3)

# **kwargs (keyword argument)

def addition(**kwargs):
    # print(kwargs)
    # print(type(kwargs)) # dict
    return sum(kwargs.values())

result  = addition (a = 1, b = 2, c = 3)
print(result)