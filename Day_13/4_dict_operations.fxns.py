# Membership Operation
# Membership is checked only in dictionary keys but not vlaue
student = {'name': 'Jane', 'age': 23, 'faculty': 'CS'}
print("name" in student) #True
print("Jane" in student) #False
print("age" not in student) #False


# Built-in functions 

print(len(student)) #3

result = sorted(student)
print(result) # ['age', 'faculty', 'name']


print(str(student)) # it makes str from dict# {'name': 'Jane', 'age': 23, 'faculty': 'CS'}