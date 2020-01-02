from matrix import generate_matrix_dimenssion


def max_element(two_dimension_array):
    max = None
    for i in two_dimension_array:
        for j in i:
            if max == None or max < j:
                max = j
    return max


def sum_of_elements(matrix):
    sum = 0
    for i in matrix:
        for j in i:
            sum += j
    return sum


def get_romb(matrix):
    new_matrix = generate_matrix_dimenssion(len(matrix))
    mid = len(matrix) // 2
    i, j = mid, mid
    new_matrix[0].append(matrix[0][mid])
    new_matrix[-1].append(matrix[-1][mid])
    for x in range(1, len(matrix)-1):
        if x > mid:
            i += 1
            j -= 1
            new_matrix[x] = matrix[x][i:j+1]
        else:
            i -= 1
            j += 1
            new_matrix[x] = matrix[x][i:j+1]


    return new_matrix
