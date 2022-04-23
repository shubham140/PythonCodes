def swapelements(lst,pos1,pos2):

    a=lst[pos1]
    b=lst[pos2]
    lst[pos2]=a
    lst[pos1]=b
    print(lst)


swapelements([1,2,3,4,5,6],1,4)