message = "hello world"


######### Strings Methods ########

#capitalize()
result = message.capitalize()
print(result)


#title()
result = message.title()
print(result)


#upper()
result = message.upper()
print(result)

#lower()
result = message.lower()
print(result)

#split()
result = message.split() # space bata split garera list ma result dinxa
print(result) 

result = message.split('o')  # ["hell", " w", "rld"] o lai xodera aru sabai aauxa split hudai 
print(result)

message = "I,am,learning,python"
result = message.split(",") # , xodera baki print hunxa as on list 
print(result) 



# join()

message = ['I', 'am', 'learning', 'python']
result = " ".join(message) # yo garesi space le join garera list lai string ma print garxa
print(result)  # I am learning python 

# message.join(" ") # this raises error

"""
# task 

# result should be  ==> I, am, learning, python

message = ['I', 'am', 'learning', 'python']
result = ", ".join(message)
print(result)

"""


# find()

message = "hello world"
result = message.find("l")
print(result) #2

result = message.find("wor")
print(result) #6

result = message.find("Wor") # navayeko diyo vane default value -1 result aauxa
print(result) #-1



# replace()

message = "hello world"
result = message.replace("hello", "HELLO")
print(result)

