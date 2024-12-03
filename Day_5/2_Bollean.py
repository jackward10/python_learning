# True and False are the Boolean Datatype . True and False are also keywords in Python
# Boolean type in python is the subclass of the Integer class
# Where False represents 0 and True represents 1.





# Relational Operators Yield Boolean Type 
a = 5
b = 3
print(a > b) # True
print(b < a) # True
print(b == a) # False
print(b != a) # True


# Logical Operator Yield boolean type
print(a > b and a != b) #True
print(b > a and a != b) #True
print(a == b and a < b) #True
print(not a ) #False
print(not b ) #False

c = None
print(not c) #True
print(not []) #True
print(not {}) #True
print(not "") #True
print(not False) #True
print(not True) #False



# membership Operations yield boolean 
print(2 in[1,2,3]) #True
print("a" not in ["a","e","i", "o", "u"]) #False

# Indentity Operation Yield Boolean
a = [1,2,3]
b = a
print(a is b)  # True
print(id(a) == id(b)) #True
print(a is not b)  # False


b = a.copy
print(a is b) #false
print(id(a) == id(b)) #False
print(a is not b) #True



# We have already mentioned , boolean is a subclass of int type.
# Let's see some examples 

print(True + 2)  # 1+2 = 3
print(70 * False)  # 70*0 = 0
print(True + True)  # 1+1 = 2
print(True + False)  # 1+0 = 1



# We have bool() built-in function for the boolean type
# Anything truthy inside the bool() function gived True and whereas anything falsy inside bool() gives False

# Any non-empty datatypes are considered truthy . Examples of truthy are :

a = 23 #(zereo bahek aru sabai truthy)
b = 12.1 #(non emty /zero float)
c = [1,2,3] # it's a non-empty list
d = (1,2,3) # It's a non-empty tuple
e = {1,2,3}  # It's a non-empty set
f = {"name":"jon", "age":23} # It's a non-empty dictionary 
g = True

print(bool(a)) #True
print(bool(b)) #True
print(bool(c)) #True
print(bool(d)) #True
print(bool(e)) #True
print(bool(f)) #True
print(bool(g)) #True


# All the empty datatypes , None and false are False

a = 0
b = 0.0
c = []
d = ()
e = {}
f = set()
g = ""
h = None
i = False
bool()

print(bool(a)) #False
print(bool(b)) #False
print(bool(c)) #False
print(bool(d)) #False
print(bool(e)) #False
print(bool(f)) #False
print(bool(g)) #False
print(bool(h)) #False
print(bool(i)) #False