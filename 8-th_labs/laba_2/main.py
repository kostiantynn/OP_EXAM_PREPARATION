from matrix import generate_random_matrix, print_formatted_matrix
from logic import fill_new_matrix


def main():
    n = int(input("n: "))
    matrix = generate_random_matrix(n)
    print_formatted_matrix(matrix, 'Before:')
    new_matrix = fill_new_matrix(matrix, n)
    print_formatted_matrix(new_matrix, 'After:')


if __name__ == '__main__':
    main()
