from logic import skalyar_multiplication
from matrix import generate_random_matrix, print_formatted_matrix


def main():
    matrix = generate_random_matrix(int(input("Length of matrix: ")))
    print_formatted_matrix(matrix, 'Before:')
    vector = skalyar_multiplication(matrix)
    print(vector)

if __name__ == '__main__':
    main()
