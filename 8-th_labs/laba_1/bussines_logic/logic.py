from . import add
from . import matrix_sum


def process_new_matrix(matrix):
    sum = matrix_sum.sum_of(matrix)
    sums = add.add_row_column(matrix)

    for i in range(len(matrix)):
        matrix[i].append(sums[0][i])
    matrix.append([sums[1][j] for j in range(len(matrix[0])-1)])
    matrix[-1].append(sum)
    return matrix
