def sum_of_elements(array):
    sum = 0
    for x in array:
        sum += abs(x)
    return sum


def min_element(array):
    min = None
    for x in array:
        if min == None or min > x:
            min = x
    return min


def get_diagonal_elements(matrix):
    array_of_diagonal_elements = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] < 0:
                array_of_diagonal_elements.append(matrix[i][i])
    return [matrix, array_of_diagonal_elements]


def sort_rows_of_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)-1):
            if matrix[i][j] < matrix[i][j+1]:
                matrix[i][j], matrix[i][j+1] = matrix[i][j], matrix[i][j+1]
    return matrix


def get_lovest_matrix(A_matrix, B_matrix, C_matrix):
    dict_of_sum = {}
    array_of_matrix = [A_matrix, B_matrix, C_matrix]
    for i in array_of_matrix:
        diagonal = get_diagonal_elements(i)
        dict_of_sum[sum_of_elements(diagonal[1])] = diagonal[0]
    minimal_sum = min_element(dict_of_sum.keys())
    return minimal_sum, dict_of_sum[minimal_sum]
