n=5
for i in range(n):
    for j in range(0,i+1):
        print("*",end=' ')
    print()
for i in range(n):
    for j in range(i,n-1):
        print("*",end=' ')
    print()

