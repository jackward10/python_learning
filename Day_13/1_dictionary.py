# Dictonary is the mutable data-type in python
# They have the elements in key-value pair format
# It is also the sequential datatype like list and tuple


# Creating an empty dictionary 

a = dict() # empty dictionary 
a = {} # This is also an empty dictionary 




# Creating a non-empty dictioanry 
#method_1
student = {"name": "Jon", "age": 23, "faculty": "CS"}
print(student) #{"name": "Jon", "age": 23, "faculty": "CS"}

#method_2
student = dict(name = "Jon", age = 23, faculty = "CS")
print(student)

#method_3
student = dict({"name": "Jon", "age": 23, "faculty": "CS"})
print(student)


#method_4
student = dict([("name", "Jon"), ("age", 23), ("faculty", "CS")])
print(student)


#  Creating a List of dictionaries

students = [
    {"name": "Jon", "age": 23, "faculty": "CS"},
    {"name": "Ram", "age": 22, "faculty": "IT"},
    {"name": "Shivu", "age": 33, "faculty": "SM"},
]

print(students)