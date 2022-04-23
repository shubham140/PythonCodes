#Code to find sum and average of elements in list anf to multiply all elements in list




def sumAndAvg(lst):
    sum=0
    avg=0
    mul1=1

    for i in lst:
        sum+=i
        mul1*=i

    avg=sum/len(lst)
    print("Sum of elements in list is {}".format(sum))
    print("Average of elements in list is {}".format(avg))
    print("Multiply of elements in list is {}".format(mul1))


sumAndAvg([1,3,4,5,6,7,8,9,12])

