def print_formatted_matrix(matrix, text):
    print(text)
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))
    print('\n\n')
