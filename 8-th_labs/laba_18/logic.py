def sort_by_minimal(matrix):
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            for x in range(len(matrix)-1):
                if matrix[x][j] > matrix[x+1][j]:
                    matrix[x][j], matrix[x+1][j] = matrix[x+1][j], matrix[x][j]
    return matrix
