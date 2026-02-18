"""
Program: Prime Number Checker
Objective:
    This program checks whether a given number is prime or not.
"""

# Taking input from the user
num = int(input("Enter a number: "))

# Numbers less than or equal to 1 are not prime
if num <= 1:
    print("Not a prime number")

else:
    is_prime = True   # Assume number is prime initially

    # Loop from 2 to square root of number (optimized check)
    for i in range(2, int(num**0.5) + 1):

        # Check divisibility
        if num % i == 0:
            is_prime = False
            break   # Stop checking once divisor found

    # Final result
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")