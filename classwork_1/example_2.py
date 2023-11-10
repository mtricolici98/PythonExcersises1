sum = 0
while sum < 1000:
    the_input = input('Say smth: ')
    sum += int(the_input)
    print(sum)

running = True
while running:
    if input() == 'stop':
        running = False

