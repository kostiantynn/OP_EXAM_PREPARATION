from isdigit import isdigit


def isalpha(string):
    for i in string:
        if isdigit(i):
            return False
    else: return True
