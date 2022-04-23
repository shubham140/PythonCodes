

def meandering_order(lst1):
    print("input is ", lst1)
    lst2=list()
    for i in range(len(lst1)):
        a=max(lst1)
        b=min(lst1)
        if(a!=b):
            lst2.append(a)
            lst2.append(b)
            lst1.remove(a)
            lst1.remove(b)
        else:
            lst1.remove(a)
            lst2.append(a)
            break


    print("Output after meandering order",lst2)
a = [-1,1,2,3,-5]
meandering_order(a)
