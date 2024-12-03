# TASK / EXAMPLE

#Given a list a = [(4,12,5),(6,1),(11,12),(6,7,8)] sort the list based on the last item of each tuple inside the list 


a = [(4,12,5),(6,1),(11,12),(6,7,8)]

def sort_with_last_number(data):
    return data[-1]

a.sort(key=sort_with_last_number)
print(a)