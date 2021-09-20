def is_leap_year(a_year):
    """
    This function will run a if statement dividing the input year by
    4 and check if the answer has a remainder of 0. If so it returns
    True if not it returns False.
    :param a_year: a single int
    :return: True or False
    """
    if a_year % 4 == 0:
        return True
    else:
        return False


input_year = int(input('Input a year to check if it is a leap year: '))

if is_leap_year(input_year):
    print('It is a leap year.')
else:
    print('It is not a leap year.')
