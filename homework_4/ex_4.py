"""
Write a program that uses a for loop to iterate through numbers from 1 to 20.
For each number, check if it's even. If it's even, print the number.
"""

# An even number is a number that divided by 2 has no remainder

# Modulo (%) uses to check what is the remained of a division.

# Example: 3 % 2 == 1 (1 is the remainder)
# Example: 4 % 2 == 0 (There is no remainder)

for number in range(1, 100):
    if number % 2 == 0:
        print(f"Number: {number} is even")
    else:
        print(f"Number: {number} is odd")
