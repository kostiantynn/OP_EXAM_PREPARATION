from matrix import generate_random_matrix, print_formatted_matrix
from logic import cut_matrix_diagonaly, max_value, index_of_max_value, delete_column


def main():
    matrix = generate_random_matrix(int(input("Enter n: ")))
    print_formatted_matrix(matrix, "Standart matrix:")
    cut_matrix = cut_matrix_diagonaly(matrix)
    print_formatted_matrix(cut_matrix, "Cut matrix:")
    max = max_value(cut_matrix)
    index_max = index_of_max_value(matrix, max)
    print("Max element:", max)
    new_matrix = delete_column(index_max, matrix)
    print_formatted_matrix(new_matrix, "New matrix:")


if __name__ == "__main__":
    main()
