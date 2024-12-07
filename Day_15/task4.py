# WAP to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number.


# Solution

total_hours = float(input("Enter the number of hours worked "))
pay_per_hour = float(input("Enter the hourly rate "))

if total_hours <= 40:
    pay = total_hours * pay_per_hour
else:
    over_time = total_hours - 40
    ot_pay = over_time * 1.5 * pay_per_hour
    normal_pay = 40 * pay_per_hour
    pay = ot_pay + normal_pay
print(pay)
