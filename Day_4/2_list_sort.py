# sort() method is used to sort the elements of the list in ascending or descending order and alphabetically for strimgs.

numbers = [8,3,6,1,7,9,4,5,2]
numbers.sort()  #it sort the numbers in ascending 
print(numbers)


numbers.sort(reverse=True) # descending number sort 
print(numbers)


numbers = [(5,4),(3,2), (1,9), (6,1)]
# Expected result [(6,1), (3,2), (5,4),(1,9)]


def sort_with_second_item(data):
    return(data[1])

numbers.sort(key=sort_with_second_item)
print(numbers)


a = [(4,12,5),(6,1),(11,12),(6,7,8)]

def sort_with_last_number(data):
    return data[-1]

a.sort(key=sort_with_last_number)
print(a)

fruits = ['banana', 'apple', 'orange', 'mango']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)