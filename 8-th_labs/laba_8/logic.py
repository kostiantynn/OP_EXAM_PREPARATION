def max_elem(array):
    max = None
    for x in array:
        if max == None or max < x:
            max = x
    return max


def sum_of_elements(two_dimension_array):
    sum = 0
    for i in two_dimension_array:
        for j in i:
            sum += j
    return sum


def cut_matrix(matrix):
    new_matrix = matrix.copy()
    j = len(matrix)
    for i in range(len(matrix)):
        new_matrix[i] = new_matrix[i][i+1:j]
    return new_matrix


def justify_sum_of_elements(A_matrix, B_matrix, C_matrix):
    sum_dictionary = {}
    matrix_array = [A_matrix, B_matrix, C_matrix]
    for x in matrix_array:
        sum = sum_of_elements(cut_matrix(x))
        sum_dictionary[sum] = x
    max_element = max_elem(sum_dictionary.keys())
    return max_element, sum_dictionary[max_element]


def replacement(matrix, elem):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] < 0:
                matrix[i][j] = elem
    return matrix
