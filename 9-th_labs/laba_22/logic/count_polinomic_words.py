from .is_polinom import is_polinom


def count_polinoms(arr_of_words):
    polinoms = []
    for word in arr_of_words:
        if is_polinom(word):
            polinoms.append(word)
    return len(polinoms)
