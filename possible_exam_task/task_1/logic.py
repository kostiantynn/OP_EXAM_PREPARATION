from rotate import rotate_matrix


def cut_matrix_in_four(matrix):
    n = len(matrix) // 2
    result = [[] for i in range(4)]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i > n - 1:
                if j > n - 1:
                    result[3].append(matrix[i][j])
                else:
                    result[2].append(matrix[i][j])
            else:
                if j > n - 1:
                    result[1].append(matrix[i][j])
                else:
                    result[0].append(matrix[i][j])
    return result


def make_matrix(arr, dimension):
    matrix = [[] for x in range(dimension)]
    j = 0
    for i in range(len(arr)):
        if i % dimension == 0 and i != 0:
            j += 1
        matrix[j].append(arr[i])
    return matrix


def rotated_matrix(array_matr):
    for i in range(len(array_matr)):
        array_matr[i] = rotate_matrix(array_matr[i], 3)
    return array_matr


def make_matr_array(arr_of_numbers, dimension):
    arr_of_matrix = [[] for i in range(4)]
    for i in range(len(arr_of_matrix)):
        arr_of_matrix[i] = make_matrix(arr_of_numbers[i], dimension)
    return arr_of_matrix
