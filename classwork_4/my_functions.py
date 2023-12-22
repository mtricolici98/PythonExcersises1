# A function that does the addition of a list of numbers

def sum_list(a_list):
    list_sum = 0
    for element in a_list:
        list_sum += element
    # print(list_sum)
    return list_sum


#
# sum_list([1, 2, 3])
#
# sum_list([5, 4, 3])
#
# value_from_input = input("")

sum_of_list = sum_list([1, 2, 4])
print(sum_of_list)



def make_pants():
    print('######')
    print('##  ##')
    print('##  ##')
    print('##  ##')
    print('##  ##')


make_pants()
