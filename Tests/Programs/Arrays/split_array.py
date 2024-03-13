from array import *
def meth(arr):
    n=len(arr)
    z=int(n/2)
    arr2=[]
    arr3=[]
    arr4=[]
    for i in range(1,z+1):
        arr2.append(i)
    print(arr2)
    for j in range(z+1,n+1):
        arr3.append(j)
    print(arr3)
    arr4=arr3+arr2
    print(arr4)

arr=[1,2,3,4,5,6]
meth(arr)