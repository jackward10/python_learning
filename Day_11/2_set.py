# Set in python are mutable. However , every elements of set must be immutable 


# Creating an empty set 
a = set() # This is a proper way of creating an empty list 
# a = {} # This is not an empty set rather it is a dictionary


# Creating non-empty set
a = set([1,2,3,4])
print(a) # {1,2,3,4}

a = {1, 2, "1", "b", "apple", True}
print(a)


# Set only takes unique elements
print(set([1, 2, 2, 3, 3, 4, 4])) # {1,2,3,4}


