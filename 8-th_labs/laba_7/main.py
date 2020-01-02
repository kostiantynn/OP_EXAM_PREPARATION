from matrix import generate_random_matrix, print_formatted_matrix
from logic import get_romb, max_element, sum_of_elements


def main():
    matrix = generate_random_matrix(int(input("Enter n: ")))
    print_formatted_matrix(matrix, "Matrix before:")
    sum = sum_of_elements(matrix)
    print("Sum of elements in matrix -", sum)
    max = max_element(matrix)
    print("Max element in matrix -", max)
    romb = get_romb(matrix)
    print_formatted_matrix(romb, 'Romb: ')


if __name__ == '__main__':
    main()
