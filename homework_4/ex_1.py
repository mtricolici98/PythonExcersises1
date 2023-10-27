"""
Write a program that asks the user to enter a character (a single letter)
The program must first check if the input was a single letter:
    If it was a single letter the program checks if it's a vowel or a consonant.
If it was not a single letter, the program displays: Can't check non-single letters.
"""

letter = input()
if len(letter) == 1:
    if letter.lower() in 'ouiyae':
        print('Vowel')
    else:
        print('Consonant')
else:
    print('Can\'t check non-single letters.')
