from matrix import generate_random_matrix, print_formatted_matrix
from logic import get_lovest_matrix, sort_rows_of_matrix


def main():
    n = int(input("Enter n: "))
    matrix_A = generate_random_matrix(n)
    print_formatted_matrix(matrix_A, 'Matrix A:')
    matrix_B = generate_random_matrix(n)
    print_formatted_matrix(matrix_B, 'Matrix B:')
    matrix_C = generate_random_matrix(n)
    print_formatted_matrix(matrix_C, 'Matrix C:')

    minimal_sum, lovest_sum_matrix = get_lovest_matrix(matrix_A, matrix_B, matrix_C)
    print('Lovest sum -', minimal_sum)

    print_formatted_matrix(sort_rows_of_matrix(lovest_sum_matrix), "Sorted lovest sum matrix:")


if __name__ == '__main__':
    main()
