from matrix import generate_random_matrix, print_formatted_matrix
from logic import sort_by_minimal


def main():
    matrix = generate_random_matrix(int(input("Enter n: ")))
    print_formatted_matrix(matrix, "Started matrix:")
    minimal_matrix = sort_by_minimal(matrix)
    print_formatted_matrix(minimal_matrix, "Minimal matrix:")


if __name__ == '__main__':
    main()
