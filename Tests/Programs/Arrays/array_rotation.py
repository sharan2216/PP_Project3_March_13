def meth(arr):
    arr2=[]
    n=len(arr)
    for i in arr:
        temp=arr[-i]
        print(temp)
        arr2.append(temp)
    print(arr2)

arr=[1,2,3,4,5]
meth(arr)