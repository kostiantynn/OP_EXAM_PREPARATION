def alghoritm(number):
    result = []
    while True:
        if number == 1:
            break
        if number <= 0:
            raise Exception("Number do not fit the task.")
        if number % 3 == 0:
            number /= 3
            result.append(3)
        else:
            number -= 5
            result.append(5)
            if number % 3 == 0 and number != 0:
                number /= 3
                result.append(3)
    return result[::-1]


def print_formatted_answer(arr_of_numbers):
    result = ['(' for x in range(len(arr_of_numbers))]
    result.append('1 ')
    for i in arr_of_numbers:
        if i == 3:
            result.append('* 3) ')
        else:
            result.append('+ 5) ')
    print(''.join(result))
