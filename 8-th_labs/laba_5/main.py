from matrix import generate_random_matrix, print_formatted_matrix
from logic import diagonal_vector, sorting_by_first_column


def main():
    matrix = generate_random_matrix(int(input("n: ")))
    print_formatted_matrix(matrix, "Standart matrix:")
    sortted_matrix = sorting_by_first_column(matrix)
    print_formatted_matrix(sortted_matrix, "Sortted matrix:")
    vector = diagonal_vector(sortted_matrix)
    print(vector)


if __name__ == '__main__':
    main()
