def max_value_in_array(array):
    max = 0
    for x in array:
        if max < x:
            max = x
    return max
