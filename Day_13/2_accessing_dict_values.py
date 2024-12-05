
# Example of accesing list : 
vowels = ['a', 'e', 'i', 'o', 'u']
print(vowels[2])

#NOW;-
# Accesing dictionary is similar to that of accesing list elements
student = {"name": "Jon", "age": 23, "faculty": "CS"}
dept = student["faculty"]
print(dept) #CS

name = student["name"]
print(name) # Jon

print(student["age"]) #23

# print(student["dob"]) #key error



# Accesing values using get() method

department  = student.get("faculty")
print(department) #cs

dob = student.get("dob")
print(dob) # None

"""
# How get function works (example)
def get(key):
    try:

        student[key]
    
    except:
        return None

"""



#  Adding key-value pair in a dictionary 

student = {"name": "Jon", "age": 23, "faculty": "CS"}
student["dob"] = "22 May"
print(student) #{'name': 'Jon', 'age': 23, 'faculty': 'CS', 'dob': '22 May'}

student.update(roll_no=12)
print(student) #{'name': 'Jon', 'age': 23, 'faculty': 'CS', 'dob': '22 May', 'roll_no': '12'}



student["name"]  = "Jane" # if value navako key rakhyo vane naya add hunxa ani value vako key rakhyo vane purano value overwrite vayera naya basxa , yesma name already xa name = Jon xa tra aba print garda yo name  = Jane hunxa 
print(student)



# Removing a key-value pair from a dictionary 

#pop() method

student = {'name': 'Jane', 'age': 23, 'faculty': 'CS', 'dob': '22 May', 'roll_no': 12}
result = student.pop("dob")
print(result) #22 May
print(student) # {'name': 'Jane', 'age': 23, 'faculty': 'CS', 'roll_no': 12}

# result = student.pop("address") # Key error
# print(result) 


#popitem() method

result = student.popitem()
print(result) # ('roll_no', 12)
print(student) # {'name': 'Jane', 'age': 23, 'faculty': 'CS'}


# clear() method 

student.clear()
print(student) # {}


# del method

del student  # deletes the object

