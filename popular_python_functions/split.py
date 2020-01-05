def split(string, pattern):
    result = []
    index_of_patterns = []
    if pattern in string:
        if string[0] != pattern and string[-1] != pattern:
            string = pattern + string + pattern
        elif string[0] != pattern and string[-1] == pattern:
            string = pattern + string
        elif string[0] == pattern and string[-1] != pattern:
            string = string + pattern
        for x in range(len(string)):
            if string[x] == pattern:
                index_of_patterns.append(x+1)
    else:
        raise Exception("Pattern did not found.")

    for i in range(len(index_of_patterns) - 1):
        result.append(string[index_of_patterns[i]:index_of_patterns[i+1]-1])
    return result
