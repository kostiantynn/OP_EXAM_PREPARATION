from matrix import generate_random_matrix, print_formatted_matrix
from logic import sort_by_diagonal, sort_by_minimal


def main():
    matrix = generate_random_matrix(int(input("Enter n: ")))
    print_formatted_matrix(matrix, "Matrix before:")
    minimal_matrix = sort_by_minimal(matrix)
    print_formatted_matrix(minimal_matrix, "Matrix after:")


if __name__ == '__main__':
    main()
