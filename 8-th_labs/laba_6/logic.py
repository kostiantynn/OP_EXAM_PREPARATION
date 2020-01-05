def m_elem(matrix):
    m_array = []
    sum = 0
    for i in matrix:
        for j in i:
            sum += j
        m_array.append(abs(sum))
        sum = 0
    return max_elem_in_array(m_array)


def max_elem_in_array(array):
    max = 0
    for x in array:
        if max < x:
            max = x
    return max


def mid_arithmetic_mNorm(A_matrix, B_matrix):
    A_norma = m_elem(A_matrix)
    B_norma = m_elem(B_matrix)
    return (A_norma + B_norma)/2
