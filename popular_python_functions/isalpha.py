from list import list


def isalpha(string):
    alphabet = list('qwertyuiopasdfghjklzxcvbnm')
    for i in string:
        if i.lower() not in alphabet:
            return False
    else: return True
