def sort_by_minimal(matrix):
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            for x in range(len(matrix)-1):
                if matrix[x][j] > matrix[x+1][j]:
                    matrix[x][j], matrix[x+1][j] = matrix[x+1][j], matrix[x][j]
    return matrix


def sort_by_diagonal(matrix):
    for i in range(len(matrix)-1):
        matrix[i+1] = get_sorted(matrix[i+1], matrix[i][i], i)
    return matrix


def get_sorted(array, element, index):
    for i in range(len(array)):
        if element < array[i]:
            array[index], array[i] = array[index], array[i]
            return array
    return array
