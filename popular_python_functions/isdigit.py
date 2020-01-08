def isdigit(string):
    try:
        chek = [int(x) for x in string]
        return True
    except:
        return False
