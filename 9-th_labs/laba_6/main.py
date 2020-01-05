from logic import count_words_of_symbvols


def main():
    string = input("Enter a sentence: ")
    pattern = input("Enter symbvols to count: ")
    count_of_words = count_words_of_symbvols(string, pattern)
    print(count_of_words, 'word with {} pattern.'.format(pattern))


if __name__ == '__main__':
    main()
