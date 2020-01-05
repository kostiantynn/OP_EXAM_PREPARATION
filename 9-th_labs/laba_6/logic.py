def split(string, pattern):
    result = []
    arr_of_index = []
    if pattern in string:
        if string[0] != pattern and string[-1] != pattern:
            string = pattern + string + pattern
        elif string[0] != pattern and string[-1] == pattern:
            string = pattern + string
        elif string[0] == pattern and string[-1] != pattern:
            string = string + pattern
        for i in range(len(string)):
            if string[i] == pattern:
                arr_of_index.append(i + 1)
    else: raise Exception("Patten was not found in the string.")
    for i in range(len(arr_of_index)-1):
        result.append(string[arr_of_index[i] : arr_of_index[i+1]-1])
    return result


def count_words_of_symbvols(string, pattern):
    arr_of_words = split(string, ' ')
    n = len(pattern)
    counter = 0
    for i in arr_of_words:
        if len(i) >= n:
            if ''.join(i[0:n]) == pattern:
                counter += 1
    return counter
