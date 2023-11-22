numbers = input('Enter Numbers').split()
max = int(numbers[0])
for nr in numbers:
    if nr > max:
        max = nr
print(max)
