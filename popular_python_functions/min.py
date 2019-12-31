def minimal_value_in_array(array):
    min = None
    for x in array:
        if min > x or min == None:
            min = x
    return min
