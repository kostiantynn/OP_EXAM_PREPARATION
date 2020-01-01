from matrix import generate_empty_matrix


def max_elem(two_dimenssion_arr):
    max = 0
    for i in two_dimenssion_arr:
        for j in i:
            if max < j:
                max = j
    return max


def cut_right(matrix, m, n):
    matrix = matrix[m:]
    m = 0
    while True:
        if m == len(matrix) - 1 or n == len(matrix) - 1:
            matrix[m] = matrix[m][:n+1]
            return matrix
        matrix[m] = matrix[m][:n+1]
        m+=1
        n+=1
    return matrix


def cut_left(matrix, m, n):
    m = 0
    while True:
        if m == len(matrix) - 1 or n == 0:
            matrix[m] = matrix[m][n:]
            return matrix
        matrix[m] = matrix[m][n:]
        n-=1
        m+=1
    return matrix


def cut_matrix(matrix, m, n):
    return cut_left(cut_right(matrix, m, n), m, n)


def fill_new_matrix(matrix, n):
    new_matrix = generate_empty_matrix(n)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_matrix[i].append(max_elem(cut_matrix(matrix, i, j)))
    return new_matrix
