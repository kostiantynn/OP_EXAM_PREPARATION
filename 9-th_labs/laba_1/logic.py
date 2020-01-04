def count_words(arr, lenght):
    words = []
    for x in arr:
        if len(x) > lenght:
            words.append(x)
    return len(words)
