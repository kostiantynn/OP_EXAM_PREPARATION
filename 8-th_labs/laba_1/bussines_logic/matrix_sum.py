def sum_of(matrix):
    sum = 0
    for i in matrix:
        for j in i:
            sum += j
    return sum
