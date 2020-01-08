from matrix.gen_matrix import generate_random_matrix
from matrix.print_matrix import print_formatted_matrix
from logic.sort_matrix_diagonal import sort_matrix_diagonal
from logic.change_positions_of_diagonals import change_diagonals


def main():
    n = int(input("Enter n: "))
    matrix1, matrix2 = generate_random_matrix(n), generate_random_matrix(n)
    print_formatted_matrix(matrix1, "First matrix:")
    print_formatted_matrix(matrix2, "Second matrix:")
    matrix1, matrix2 = change_diagonals(sort_matrix_diagonal(matrix1), sort_matrix_diagonal(matrix2))
    print_formatted_matrix(matrix1, "First matrix after:")
    print_formatted_matrix(matrix2, "Second matrix after:")


if __name__ == '__main__':
    main()
