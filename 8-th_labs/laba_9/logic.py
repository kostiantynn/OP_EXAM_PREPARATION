def get_central_element(matrix):
    n = len(matrix) // 2
    return matrix[n][n]


def change_positions_of_matrix_elements(matrix):
    n = len(matrix)//2
    i = 0
    j = len(matrix)-1
    for x in range(len(matrix)):
        matrix[i][0:i+1], matrix[i][j:len(matrix)] = matrix[i][j:len(matrix)], matrix[i][0:i+1]
        if x >= n:
            i -= 1
            j += 1
        else:
            i += 1
            j -= 1
    return matrix
