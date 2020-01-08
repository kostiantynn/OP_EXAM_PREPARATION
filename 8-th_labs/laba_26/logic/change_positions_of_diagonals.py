def change_diagonals(matrix1, matrix2):
    for i in range(len(matrix1)):
        matrix1[i][i], matrix2[i][i] = matrix2[i][i], matrix1[i][i]
    return matrix1, matrix2
