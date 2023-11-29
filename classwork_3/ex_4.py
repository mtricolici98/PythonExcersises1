# dictionary = {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": "value3",
#     "key4": "value4",
# }
#
# print(dictionary['key1'])
#
# my_key = input()
# print(dictionary[my_key])
import os

#
# for key in dictionary:
#     print(key, dictionary[key])

import os
for folder in os.listdir(os.environ.get("HOME")):
    print(folder)

print("Pictures" in os.listdir(os.environ.get("HOME")))
