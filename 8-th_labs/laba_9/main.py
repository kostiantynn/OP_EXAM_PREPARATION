from matrix import generate_random_matrix, print_formatted_matrix
from logic import get_central_element, change_positions_of_matrix_elements


def main():
    matrix = generate_random_matrix(int(input("Enter n: ")))
    print_formatted_matrix(matrix, "Started matrix:")
    central_element = get_central_element(matrix)
    print("Central element:", central_element)
    print_formatted_matrix(change_positions_of_matrix_elements(matrix), "New matrix:")


if __name__ == '__main__':
    main()
