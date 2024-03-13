def meth(arr):
    n=len(arr)
    min=arr[0]
    max=arr[n-1]
    for i in arr:
        if i<min:
            min=i
        elif i>max:
            max=i
    print(min)
    print(max)

    
arr=[4,2,3,1,6,5]
meth(arr)