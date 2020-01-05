def split(string, pattern):
    result = []
    arr_of_index = []
    if pattern in string:
        if string[0] != pattern and string[-1] != pattern:
            string = pattern + string + pattern
        elif string[0] == pattern and string[-1] != pattern:
            string = string + pattern
        elif string[0] != pattern and string[-1] == pattern:
            string = pattern + string
        for i in range(len(string)):
            if string[i] == pattern:
                arr_of_index.append(i+1)
    else:
        raise Exception("Pattern does not exist in given string.")

    for i in range(len(arr_of_index)-1):
        result.append(string[arr_of_index[i]:arr_of_index[i+1]-1])
    return result
