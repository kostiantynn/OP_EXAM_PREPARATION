def print_formatted_matrix(matrix, text):
    print(text)
    print('\n'.join([''.join(['{:4}'.format(j) for j in i]) for i in matrix]))
    print('\n\n')
