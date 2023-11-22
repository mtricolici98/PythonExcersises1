# cars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
cars = range(1, 16)
print(list(cars))
for car in cars:
    if car % 2 == 0:
        print(f"Even cars don't need to be checked, car nr {car} can go through")
    else:
        print(f'Checking the documents for car nr {car}')
        print(f'Taking the money from the driver of {car}')
        print(f'Returning the ticket to the driver of {car}')

print("I am out of the loop")
