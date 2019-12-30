from random import randint


def generate_random_matrix(m, n, a, b):
    return [[randint(a, b) for j in range(n)] for i in range(m)]
