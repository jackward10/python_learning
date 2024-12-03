# list Remove
#remove()  method
# remove method takes list item as parameter 

vowels = ["a", "e", "i", "o", "u"]
vowels.remove('e')  # it removes 'e' from list
print(vowels)

# if we pass a parameter not present in the list then it raises error

# vowels.remove('p)  # it raises value eroor

# pop() method 
# pop takes index as a parameter 

vowels = ["a", "e", "i", "o", "u"]
result = vowels.pop(2)
print(result)  #'i'
print(vowels) # ["a","e","o","u"]

#pop() method also returns a value from the index passed as the parameter
# Inthe above example result gives 'i' because 'i' is at 2nd index. and , finally 'i' is also removed from list vowels 





# clear() method . 
# It clears the list 

vowels = ["a", "e", "i", "o", "u"]
vowels.clear() # it clears the list
print(vowels) #[]


#index() method 
# It takes item as an argument

vowels = ["a", "e", "i", "o", "u"]
result = vowels.index("o")
print(result) # 3
print(vowels)

# index() method also takes start and end as parameters 
vowels = [5, 4, 10, "o", "u", 10,4]
result = vowels.index(4,2,8)
print(result) #6


#count() method takes list item as parameter and returns the number of repetition of that itema 

vowels = ["a", "e", "a", "e", "u","a", "o", "i", "o", "u"]
result = vowels.count("a")
print(result) #3
print(vowels.count("o")) #2


# reverse() method 
# It reverses the item of the list 

fruits = ['banana', 'apple', 'orange', 'mango']
fruits.reverse()
print(fruits)