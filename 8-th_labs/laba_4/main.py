from matrix import generate_random_matrix, print_formatted_matrix
from logic import cut_matrix


def main():
    matrix = generate_random_matrix(int(input("n: ")))
    print_formatted_matrix(matrix, "Before:")
    new_matrix = cut_matrix(matrix)
    print_formatted_matrix(new_matrix, "After:")


if __name__ == '__main__':
    main()
