from logic.count_polinomic_words import count_polinoms
from string_func.split import split


def main():
    string = input("Enter a string: ")
    print('Number of polinomic words in string:', count_polinoms(split(string, ' ')))


if __name__ == '__main__':
    main()
