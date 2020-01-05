def sorting_by_first_column(matrix):
    for j in range(len(matrix)):
        for i in range(len(matrix)-1):
            if matrix[i][0] < matrix[i+1][0]:
                matrix[i][0], matrix[i+1][0] = matrix[i+1][0], matrix[i][0]
    return matrix


def diagonal_vector(matrix):
    vector = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                vector.append(matrix[i][j])
    return vector
