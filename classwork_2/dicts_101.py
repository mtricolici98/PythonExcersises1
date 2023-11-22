# A small program, that translates numbers from 0 to 9 from integer to text
# Example: 1 will be 'One'
# Example: 2 will be 'Two'
numbers = [
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Zero",
]

print(numbers[9])
print(numbers[1])
print(numbers[1])

# The second way to solve this.
number = 0

if number == 0:
    print('O')
elif number == 1:
    print('1')

numbers_dict = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    0: "Zero",
}

print(numbers_dict[0])

mcdonalds_menu_list = [
    "Fries",
    "Coke",
    "Cheeseburger",
]

print(mcdonalds_menu_list[0])
print(mcdonalds_menu_list[1])

print("Dict VERSION!")

mcdonalds_menu_dict = {
    "Happy Meal": ["Cheeseburger", "Fries", "Coke", "Toy"],
    "fries": "Fries",
    "Coke": "Coke",
    "Cheeseburger": "Cheeseburger",
}

print(mcdonalds_menu_dict["Cheeseburger"])
print(mcdonalds_menu_dict["Happy Meal"])

print(mcdonalds_menu_dict)
