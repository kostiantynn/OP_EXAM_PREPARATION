from matrix import generate_random_matrix, print_formatted_matrix
from logic import mid_arithmetic_mNorm


def main():
    n = int(input("n: "))
    A_matrix = generate_random_matrix(n)
    print_formatted_matrix(A_matrix, "Matrix A:")
    B_matrix = generate_random_matrix(n)
    print_formatted_matrix(B_matrix, "Matrix B:")
    mid_norma = mid_arithmetic_mNorm(A_matrix, B_matrix)
    print("Mid Arithmetic of two norms: ", mid_norma)


if __name__ == '__main__':
    main()
