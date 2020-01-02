def max_value_in_array(array):
    max = None
    for x in array:
        if max < x or max == None:
            max = x
    return max
