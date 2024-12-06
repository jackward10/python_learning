# copy()

student = {"name": "Jon", "age": 23}
student2 = student.copy()
print(student2) # {"name": "Jon", "age": 23}
print(student)  # {"name": "Jon", "age": 23}

#get()
student = {"name": "Jon", "age": 23}
name = student.get("name")
print(name) #Jon

roll = student.get("roll")
print(roll) #None

roll = student.get("roll", 1)
print(roll) #1

nam = student.get("name", "Ram")
print(name) # Jon


# items()
student = {"name": "Jon", "age": 23}
print(student.items()) #([('name', 'Jon'), ('age', 23)])


# keys()
student = {"name": "Jon", "age": 23}
print(student.keys())# (['name', 'age'])


# values()

student = {"name": "Jon", "age": 23}
print(student.values()) # (['Jon', 23])


# pop()

student = {"name": "Jon", "age": 23, "roll": 22}
age = student.pop("age")
print(age) #23
print(student) # {"name": "Jon", "roll": 22}


# popitem()
student = {"name": "Jon", "age": 23, "roll": 22}
result = student.popitem()
print(result) # ("roll", 22)
print(student) # {'name': 'Jon', 'age': 23}


# update()
student = {"name": "Jon", "age": 23, "roll": 22}
student.update(address = "KTM")
print(student) # {'name': 'Jon', 'age': 23, 'roll': 22, 'address': 'KTM'}


# fromkeys()

a = dict()
result = a.fromkeys([1, 2], "a")
print(result) #{1: "a", 2: "a"}


#setdefault()
student = {"name": "Jon", "age": 23, "roll": 22}
student.setdefault("name", "Jane")
print(student) # {'name': 'Jon', 'age': 23, 'roll': 22}

student.setdefault("address", "BKT")
print(student) # 
{'name': 'Jon', 'age': 23, 'roll': 22, 'address': 'BKT'}

