# Write a program to prompt for a score between 0.0 and 1.0. if the score is between 0.0 and 1.0, print
# a grade using the following table :
# A for >= 0.9
# B for >= 0.8
# C for >= 0.7
# D for >= 0.6
# F for <= 0.6

# if the user enters a value out of range , print a suitable error message.


# Solution

score  = float(input("Enter a Number "))
if score > 1.0 or score <0.0:
    print("Invalid Score")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("A")
elif score >= 0.7:
    print("A")
elif score >= 0.6:
    print("A")
else:
    print("F")


