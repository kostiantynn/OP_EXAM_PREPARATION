def rotate_matrix(matrix, times):
    for x in range(times):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[j][i] = matrix[i][::-1][j]
    return matrix
