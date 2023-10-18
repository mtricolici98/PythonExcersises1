"""
The code below will generate a single random number between 1 and 10.

Create a program that will give the user 3 chances to guess the number generated.

If the user guesses the number, show "Congratulations" and finish the program using the `exit()` function.

If the user guesses a number lower than the random number, show "Higher".

If the user guesses a number higher than the random number, show "Lower"
"""

import random

random_number = random.randrange(1, 11)
