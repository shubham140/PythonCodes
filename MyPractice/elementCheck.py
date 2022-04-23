def elementCheck(lst, element):
    if (element in lst):
        return True
    else:
        return False


a=elementCheck([1, 2, 3, 4, 5, 6, 7], 10)
print(a)