from matrix import print_formatted_matrix, generate_random_matrix, check_if_dimension_right
from logic import rotated_matrix, make_matr_array, cut_matrix_in_four


def main():
    n = int(input("Enter n: "))
    if check_if_dimension_right(n):
        matrix = generate_random_matrix(n)
    print_formatted_matrix(matrix, "Started matrix: ")
    array_of_four_matrix = make_matr_array(cut_matrix_in_four(matrix), len(matrix) // 2)
    for matr in range(len(rotated_matrix(array_of_four_matrix))):
        print_formatted_matrix(array_of_four_matrix[matr], "Rotated matrix № "+ str(matr+1))


if __name__ == '__main__':
    main()
