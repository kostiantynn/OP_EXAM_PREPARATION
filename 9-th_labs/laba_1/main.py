from logic import count_words
from split import split


def main():
    string = input("Enter a sentence: ")
    lenght = int(input("Enter max lenght: "))
    words = count_words(split(string, ' '), lenght)
    print(words, "- word's lenght is bigger.")


if __name__ == '__main__':
    main()
