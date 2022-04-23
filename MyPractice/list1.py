

# This code is very basic to swap first and last elements of list
def swaplist(lst):
    a=lst[0]
    b=lst[-1]
    lst[0]=b
    lst[-1]=a
    print(lst)


swaplist(["apple","orange","mango"])