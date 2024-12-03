# Python lists are mutable objects     
# We can create a list by enclosing the sequence in Big Brackets []
# We can also create a list using () built-in function

a  =[] # An empty list 
b = list() # An empty list using list() function 

a = [1,2,3] # Non empty List 
# In this list all data are of Integer data type . But list can also have hetrogenous type

a = [ 1, "hello", 2.1, {1,2,3,}, {"a":1,"b":2} ]

# In this list , the data are of dfferent types which also supported by a python list 


# We can use built-in type() function to check the type of object
type([1,2,3]) #list
type((1,2,3)) #tuple
type(1) #int
# and so on...
