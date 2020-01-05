def add_spaces(string):
    string_arr = list(string)
    i = 0
    while True:
        if len(string_arr) == 60:
            break
        if i == len(string_arr) - 1:
            i = 0
        if string_arr[i] == ' ':
            string_arr.insert(i, ' ')
            i += 2
        i += 1
    return ''.join(string_arr)
