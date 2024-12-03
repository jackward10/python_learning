# Strings are immutable and sequence data-type in python
# Creating an empty string
# 


a = "" #empty string
a = '' #empty string
c = """""" #empty string
d = str() #empty string

# Creating a non-empty string

a = "Hello World"
b = 'Python is a high level language'
c = """
Hello world 
Python is awesome.
"""



# Quote chracters 

a = "I'm Learning Python"
b = 'He said, "Python is eaasy to learn"'

# We can also use escape chracters for in strings with quote

a = 'I\'m learning Python'
b = "He said, \"Python is easy to learn\""


# Escape chracters are the chracters in python which suppress the acutal python meaning and gives new meaning to that chracter 
# \', \", \n, \t are the examples of escape chracters

print("Hello\nWorld")  # Print Hello in first Line and world in second line
print("Hello\tWorld") # Prints Hello , a tab, and world  



# Python also has Triple quoted strings 

message = """
I'm Learning Python
"""

message = '''
I'm learning python
'''

# There is no need for \' (escape sequence) for triple quoted strinngs
# Triple quoted strimgs are not only used as normal strings, but are also used to add code descriptions,
# in functions , classes and multiline comments


def addition (a,b):
    """
    :param a : any integer value
    :param b  : any integer value
    :return : sum of a and b
    """
    return a+b

help(addition)