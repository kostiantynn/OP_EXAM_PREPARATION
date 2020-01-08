from matrix import print_formatted_matrix, generate_random_matrix


def rotate_matrix(matrix, times):
    current_matrix = [[0 for i in range(len(matrix))] for x in range(len(matrix))]
    for x in range(times):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                current_matrix[j][i] = matrix[i][::-1][j]
        matrix = current_matrix
        current_matrix = [[0 for i in range(len(matrix))] for x in range(len(matrix))]
    return matrix
