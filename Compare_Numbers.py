"""
Program: Largest of Three Numbers
Objective:
    This program finds the largest number among three numbers
    entered by the user.
"""

# Taking three numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Comparing numbers to find the largest
if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
elif c > a and c > b:
    largest = c
else:
    largest='none as all numbers are equal'
# Display the largest number
print("Largest number is ", largest)
