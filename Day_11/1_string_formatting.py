# we can format string using f-strings 

# usinf f() Krishstring method
name = input ("Enter Your Name ")
age = int(input("Enter Your Age "))
language = input ("Enter the Language You're Learning ")
message = f"Hello I am {name}. I am learning {language}"
print(message)

message = f"Hello I am {name}. I am {age} years old, I am learning {language} "
print(message)





# using Percentage %() Method
message = 'I am %s and I am %d years old ' %(name, age)
print(message)




# using format() Method

message = "I am {} and I am {} years old "
formatted_message =  message.format(name, age)
print(formatted_message)


messgae = "I have {1}, {0} and {2} in my bag ".format('book', 'pen', 'copy')
print(messgae)


# error case
# messgae = "I have {1}, {0} and {2} in my bag ".format('book', 'pen') #it raises error


messgae = "I have {} and {} in my bag ".format('book', 'pen', 'copy') #but it won't raise error
print(messgae) # here first placeholder takes 'book', second placeholder takes 'pen' and others are ignored


