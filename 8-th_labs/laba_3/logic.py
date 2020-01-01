def skalyar_multiplication(matrix):
    column_ind = matrix[0].index(max_elem(matrix[0]))
    result = []
    for i in range(len(matrix)):
        result.append(matrix[0][i] * matrix[i][column_ind])
    return result


def max_elem(arr):
    max = 0
    for x in arr:
        if max < x:
            max = x
    return max
