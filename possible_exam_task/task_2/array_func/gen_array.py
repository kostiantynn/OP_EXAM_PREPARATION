from random import randint


def gen_array(n):
    return [randint(-100, 100) for i in range(n)]
