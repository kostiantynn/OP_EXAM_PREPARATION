from logic import is_number_fit_the_task, alghoritm, print_formatted_answer


def main():
    number = int(input("Enter a number: "))
    if is_number_fit_the_task(number):
        print_formatted_answer(alghoritm(number))


if __name__ == '__main__':
    main()
