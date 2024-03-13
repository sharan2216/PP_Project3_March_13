arr=[3,2,4,6,5]
n=len(arr)
min=arr[0]

max=arr[n-1]
print(max)

for i in arr:
    if i > max:
        max=i
    elif i<min:
        min=i

print(max)
print(min)