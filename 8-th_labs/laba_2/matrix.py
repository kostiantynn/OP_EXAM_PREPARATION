from random import randint


def print_formatted_matrix(matrix, text):
    print(text)
    print("\n".join([''.join(['{:4}'.format(j) for j in i]) for i in matrix]))
    print('\n\n')


def generate_random_matrix(n):
    return [[randint(0, 100) for j in range(n)] for i in range(n)]


def generate_empty_matrix(n):
    return [[] for i in range(n)]
