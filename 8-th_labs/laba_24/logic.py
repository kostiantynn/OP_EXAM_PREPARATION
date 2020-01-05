def max_value(two_dimension_array):
    max = None
    for i in two_dimension_array:
        for j in i:
            if max == None or max < j:
                max = j
    return max


def cut_matrix_diagonaly(matrix):
    new_matrix = matrix.copy()
    for i in range(len(new_matrix)):
        new_matrix[i] = new_matrix[i][i+1:len(new_matrix)]
    return new_matrix


def index_of_max_value(matrix, max):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == max:
                return j


def delete_column(index_of_column, matrix):
    for i in range(len(matrix)):
        matrix[i].pop(index_of_column)
    return matrix
