def add_row_column(matrix):
    sum_of_rows = [sum(i) for i in matrix]
    sum_of_columns = []
    for column in range(len(matrix[0])):
        s = 0
        for row in matrix:
            s += row[column]
        sum_of_columns.append(s)
    return sum_of_rows, sum_of_columns
