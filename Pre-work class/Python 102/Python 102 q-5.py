number_list_all = [[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 4, 5], [5, 6, 7, 8], [52, 63, 75, 36],
                   [102, 103, 104, 105, 106]]

def is_consecutive(a_list):
    """
    This function will take a list of int numbers and compare the
    first number in the list +1 to the second. This will loop until
    the number being check is == the max number in the list. If so
    is_consecutive will return True. If the check fails is_consecutive
    will return False.

    :param a_list: A list of int numbers...
    :return: True or False
    """
    number_check = min(a_list)
    max_number = max(a_list)
    for number in a_list[1:]:
        if number == max_number:
            return True
        elif number == number_check + 1:
            number_check += 1
        else:
            return False


print('Python will now check all the provided lists for consecutive numbers.\n')
for list in number_list_all:
    print('Checking list:\n' + str(list))
    print(is_consecutive(list))
