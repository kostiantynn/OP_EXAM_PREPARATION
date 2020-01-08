from random import randint


def generate_random_matrix(n):
    return [[randint(-100,100) for j in range(n)] for i in range(n)]
