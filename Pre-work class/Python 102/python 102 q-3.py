number_list = [13, 14, 66, 77, 64, 333, 7, 98, 5567, 55555, 55556]
number_list2 = [13, 14, 66, 77, 100000000, 2, 4343, 6457]
number_list3 = [1, 22, 33, 44, 55, 666]
number_list_all = [[13, 14, 66, 77, 64, 333, 7, 98, 5567, 55555, 55556],
                   [13, 14, 66, 77, 100000000, 2, 4343, 6457], [1, 22, 33, 44, 55, 666]]

def max_num_in_list(a_list):
    """
    This function uses a for loop to go through a list and compare
    each number to max_number which is default set to 0.
    It will return the max number.
    :param a_list:
    :return: Max number in a given list as int
    """
    max_number = 0
    for number in a_list:
        if number > max_number:
            max_number = number

    return max_number

for list in number_list_all:
    print('Checking for a max number with function 1 with list:\n'
          + str(list))
    print('Max number is: ' + str(max_num_in_list(list)))

# OR


def max_num_in_list2(a_list):
    """
    This function uses the max() function to return the max
    number in a given list.
    :param a_list:
    :return: Max number in given list as int
    """
    return max(a_list)


for list in number_list_all:
    print('Checking for a max number with function 2 with list:\n'
          + str(list))
    print('Max number is: ' + str(max_num_in_list2(list)))
