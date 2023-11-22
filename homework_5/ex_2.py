my_string = input('Input your string')

# Long Way
# Prepending
reverse_string = ''
for char in my_string:
    reverse_string = char + reverse_string

print(reverse_string)

# Long Way
# Appending
reverse_string = ''
for index in range(1, len(my_string) + 1):
    reverse_string += my_string[-index]

print(reverse_string)

## Short way
reverse_string = my_string[::-1]
print(reverse_string)
