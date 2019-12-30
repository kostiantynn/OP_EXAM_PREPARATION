from matrix.generate_matrix import generate_random_matrix
from matrix.print_matrix import print_formatted_matrix
from bussines_logic.logic import process_new_matrix


def main():
    m, n = int(input("M-rows: ")), int(input("N-columns: "))
    a, b = int(input("From a: ")), int(input("To b: "))
    matrix = generate_random_matrix(m, n, a, b)
    print_formatted_matrix(matrix, 'Started matrix:')
    new_matrix = process_new_matrix(matrix)
    print_formatted_matrix(new_matrix, 'New matrix:')

if __name__ == '__main__':
    main()
