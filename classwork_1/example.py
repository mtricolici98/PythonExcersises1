running = True
sum = 0
while running:  # Only True/False
    the_input = input('Say smth: ')
    if the_input == 'STOP':
        running = False
    else:
        sum += int(the_input)
    print(sum)
