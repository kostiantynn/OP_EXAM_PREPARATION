def split(string, pattern):
    result = []
    array_of_index = []
    if pattern in string:
        if string[0] != pattern and string[-1] != pattern:
            string = pattern + string + pattern
        elif string[0] == pattern and string[-1] != pattern:
            string = string + pattern
        elif string[0] != pattern and string[-1] == pattern:
            string = pattern + string
        for i in range(len(string)):
            if string[i] == pattern:
                array_of_index.append(i+1)
        for i in range(len(array_of_index)-1):
            result.append(string[array_of_index[i] : array_of_index[i+1]-1])
    else: raise Exception("Pattern does not exist in string.")
    return result
