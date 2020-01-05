from random import randint


def generate_random_matrix(n):
    return [[randint(0,99) for j in range(n)] for i in range(n)]


def print_formatted_matrix(matrix, text):
    print(text)
    print('\n'.join([''.join(['{:4}'.format(j) for j in i]) for i in matrix]))


def check_if_dimension_right(lenght):
    if lenght % 2 == 0 and lenght != 1:
        return True
    else: raise Exception("Given leangth of matrix is not right.")
