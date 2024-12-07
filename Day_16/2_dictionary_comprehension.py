squared = {data: data**2 for data in range (1, 13)}
print(squared)

student_list = [("name", "Jon"), ("age", 25), ("address", "ktm")]
student = dict(student_list)
print(student)

# Create dictionary for the above data using dictionary comprehension
student = {key: value for key, value in student_list}
print(student)

