# name = 'Sparky'
# type = 'Dog'


# animal_1 = {
#     'name': "Sparky",
#     "type": 'Dog'
# }
#
# animal_2 = {
#     'name': "Panther",
#     "type": 'Cat'
# }
#
#
# def sleep(animal):
#     print(f"{animal['name']} is sleeping")
#
#
# sleep(animal_1)
# sleep(animal_2)


class Animal:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def sleep(self):
        print(f"{self.type} {self.name} is sleeping")


my_dog = Animal('Sparky', 'Dog')
print(my_dog.name)
print(my_dog.type)
my_dog.sleep()
my_dog.name = 'Barky'
my_dog.sleep()

my_cat = Animal('Panther', 'Cat')
print(my_cat.name)
print(my_cat.type)
my_cat.sleep()
