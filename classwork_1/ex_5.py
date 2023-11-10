"""
The code below will generate a single random number between 1 and 10.

Create a program that will give the user 3 chances to guess the number generated.

If the user guesses the number, show "Congratulations" and finish the program using the `exit()` function.

If the user guesses a number lower than the random number, show "Higher".

If the user guesses a number higher than the random number, show "Lower"
"""

import random

should_play = True

while should_play:
    random_number = random.randrange(1, 11)
    print(random_number)
    for a in range(3):
        print(f"Attempt {a + 1} out of 3")
        guess = int(input('Your guess?'))
        if guess > random_number:
            print('Lower')
        elif guess < random_number:
            print('Higher')
        else:
            print("Congratulations")
            break
    if guess != random_number:
        print(f"You've lost")

    print('You wanna play again ?')
    should_play = input('Y/N?').lower() == 'y'

print("Good bye!")