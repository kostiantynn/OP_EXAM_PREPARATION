def __find_same__(string):
    arr_index = []
    for i in range(len(string)):
        for j in range(len(string)):
            if string[i] == string[j] and i != j:
                arr_index.append(i)
                arr_index.append(j)
    return set(arr_index)


def delete_same(string):
    delete_index_arr = __find_same__(string)
    l_string = list(string)
    j = 0
    for i in delete_index_arr:
        i -= j
        l_string.pop(i)
        j+=1
    return ''.join(l_string)
