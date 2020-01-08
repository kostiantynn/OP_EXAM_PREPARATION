def sort_matrix_diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)-1):
            if matrix[j][j] > matrix[j+1][j+1]:
                matrix[j][j], matrix[j+1][j+1] = matrix[j+1][j+1], matrix[j][j]
    return matrix
