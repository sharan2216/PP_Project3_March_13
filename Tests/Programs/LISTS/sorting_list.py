l=[3,5,2,1,8,7]
n=len(l)
for i in range(n):
    for j in range(i+1,n):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]

print(l)