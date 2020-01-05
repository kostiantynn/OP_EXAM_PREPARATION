def max_element_by_abs(matrix):
    max = 0
    for i in matrix:
        for j in i:
            if max < abs(j):
                max = j
    return max


def find_element(matrix):
    max_elem = max_element_by_abs(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == max_elem:
                return i, j


def cut_matrix(matrix):
    i, j = find_element(matrix)
    for x in range(len(matrix)):
        matrix[x].pop(j)
    matrix.pop(i)
    return matrix
