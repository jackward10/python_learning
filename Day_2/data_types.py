# Mutable and Imutable objects

'''
If an object once created can be changed later then the object is Mutable .
But if an onject once created can never changed throught it's life cycle it's an Imutable object.


List , Dictonary , Set are the example of Mutable objects .   
Numbers, Tuple , Boolean, Strings  are the example of Imutbale object .

'''

# example 

a = ['a', 'b','c', 'd']
a[3] = 'z'
print(a) # the value of 'd' chnaged as 'z'

b = (1,2,3,4)
b[2] = 9
print(b) #it raises eroor because tuple is imutable 
