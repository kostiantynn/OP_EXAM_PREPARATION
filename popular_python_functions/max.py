def max_value_in_array(array):
    max = None
    for x in array:
        if max == None or max < x:
            max = x
    return max
