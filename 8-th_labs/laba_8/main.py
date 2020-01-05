from matrix import generate_random_matrix, print_formatted_matrix
from logic import justify_sum_of_elements, replacement


def main():
    n = int(input("Enter n: "))
    matrix_A = generate_random_matrix(n)
    print_formatted_matrix(matrix_A, 'Matrix A:')
    matrix_B = generate_random_matrix(n)
    print_formatted_matrix(matrix_B, 'Matrix B:')
    matrix_C = generate_random_matrix(n)
    print_formatted_matrix(matrix_C, 'Matrix C:')

    max_sum, matrix = justify_sum_of_elements(matrix_A, matrix_B, matrix_C)
    print('Max sum:', max_sum)

    replaced_matrix = replacement(matrix, max_sum)
    print_formatted_matrix(replaced_matrix, "Replaced matrix: ")

if __name__ == '__main__':
    main()
